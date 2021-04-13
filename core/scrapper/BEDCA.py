import requests
from lxml import etree

from core.models import FoodGroup, Food, Component, ComponentGroup, ComponentType


class Node():
    @staticmethod
    def childTexts(node):
        texts = {}
        for child in list(node):
            texts[child.tag] = child.text
        return texts


class BEDCAScrapper():
    url = None
    headers = {"content-type": "text/xml;charset=UTF-8"}
    group_request_file = "./resources/group.xml"
    foodprofile_request_file = "./resources/food_profile.xml"
    group_list_request_file = "./resources/group_list_by_id.xml"
    component_request_file = "./resources/component_group.xml"

    def __init__(self, url):
        if url:
            self.url = url
        else:
            raise ValueError

    def import_request_from_file(self, path):
        with open(path, 'r') as file:
            result = file.read()
        if result:
            return result

    def response2dict(self, tree, keyword):
        result = []
        for elm in tree.xpath(keyword):
            data = Node.childTexts(elm)
            result.append(data)
        return result

    def import_component_groups(self):
        component_group = self.import_request_from_file(self.component_request_file)
        response = requests.post(self.url, data=component_group, headers=self.headers)
        tree = etree.fromstring(response.content)
        results = self.response2dict(tree, keyword="//foodresponse/food/foodvalue")
        for result in results:
            cg, created = ComponentGroup.objects.get_or_create(id=result['cg_id'],
                                                               es_description=result['cg_descripcion'],
                                                               en_description=result['cg_description'])
            if created:
                cg.save()

    def import_component_types(self):
        component_group = self.import_request_from_file(self.component_request_file)
        response = requests.post(self.url, data=component_group, headers=self.headers)
        tree = etree.fromstring(response.content)
        results = self.response2dict(tree, keyword="//foodresponse/componentList/component")
        for result in results:
            ct, created = ComponentType.objects.get_or_create(id=result['id'],
                                                              es_description=result['name_esp'],
                                                              en_description=result['name_ing'])
            if created:
                ct.save()

    def import_food_groups(self):
        group_request = self.import_request_from_file(self.group_request_file)
        response = requests.post(self.url, data=group_request, headers=self.headers)
        tree = etree.fromstring(response.content)
        results = self.response2dict(tree, keyword="//foodresponse/food")
        for result in results:
            food, created = FoodGroup.objects.get_or_create(id=result['fg_id'], es_description=result['fg_ori_name'],
                                                            en_description=result['fg_eng_name'])
            if created:
                food.save()

    def import_foods(self):
        for group in FoodGroup.objects.all():
            list_food = self.import_request_from_file(self.group_list_request_file)
            list_food = list_food.replace("$ID", str(group.id))
            response = requests.post(self.url, data=list_food, headers=self.headers)
            tree = etree.fromstring(response.content)
            results = self.response2dict(tree, keyword="//foodresponse/food")
            for result in results:
                food, created = Food.objects.get_or_create(id=result['f_id'], es_description=result['f_ori_name'],
                                                           en_description=result['f_eng_name'], group=group)
                if created:
                    food.save()

    def import_food_profile(self):
        for food in Food.objects.all():
            list_profile = self.import_request_from_file(self.foodprofile_request_file)
            list_profile = list_profile.replace("$ID", str(food.id))
            response = requests.post(self.url, data=list_profile, headers=self.headers)
            tree = etree.fromstring(response.content)
            results = self.response2dict(tree, keyword="//foodresponse/food/foodvalue")
            for result in results:
                try:
                    type, created = ComponentType.objects.get_or_create(id=result['c_id'],
                                                                        es_description=result['c_ori_name'],
                                                                        en_description=result['c_eng_name'])
                    record, created = Component.objects.get_or_create(type=type,
                                                                      value=result['best_location'],
                                                                      meassure=result['v_unit'])
                    if created:
                        record.save()
                        food.components.add(record)
                except Exception as err:
                    raise err
