# -*- coding:utf-8 -*-

'''
    Creator : Ayouba Anrezki
    Initialization : 29/10/2022  at 22h28
    Name : COR
    Objective : give the formulas (Lewis, semi-developed, raw, topological) , 
                identify characteristic groups,  identify family (function) , 
                give name from formulas, give formulas from name, 
                identify molecule from spectrum , 
    Modules : math, random, tkinter, matplotlib
'''

#IMPORT
import math
import random
import tkinter
import matplotlib

class Formulas:
    '''
        the formule of your molecule
    '''
    def __init__(self, formula) -> None:
        self.formula_type = formula[0]
        self.formula = formula[1]
    
    def to_usable_form(self):
        if self.formula_type == "carbon_chain":
            usable_form =  ""
            for i in range(len(self.formula)):
                if not self.formula[i] in ["{}".format(i) for i in range(10)] and not (self.formula[i] == "H" and (i > 0 and self.formula[i-1] == "C")):
                    usable_form += self.formula[i]
            return ("usable_form", usable_form)
    
    def to_carbon_chain(self):
        pass

    def to_semi_developed(self):
        pass

    def to_topological(self):
        pass

class GroupsFamily(Formulas):
    '''
        the characteristic groups, and the family (funtion)
    '''
    familyandgroup = {
                        "Alcool":["OH", "hydroxyle"],
                        "Aldhéhyde":["C(=O)H", "Carbonyle"],
                        "Cétone":["C=O","Carbonyle"],
                        "Acide_carboxylique":["C(=O)-OH", "Carboxyle"],
                        "Alcène":["C=C", "Alcène"],
                        "Ester":["C(=O)O", "Ester"],
                        "Amine":["C-N","Amine"],
                        "Amide":["C(=O)-N","Amide"]
                     }
    
    def __init__(self, formula) -> None:
        super().__init__(formula)
        self.usable_form_formula = self.to_usable_form()[1]

    def identify(self):

        def jumper(char):
            table_jump = {}
            for i in range(len(char)-1):
                table_jump[char[i]] = (len(char)-1)-i
            return table_jump

        groups = [group[0] for group in list(self.familyandgroup.values())]
        molecul_groups = []
        formula = list(self.usable_form_formula)
        length_formula = len(formula)

        for group in groups:
            list_group = list(group)
            length_group = len(list_group)
            if length_group < length_formula:
                jump = jumper(list_group)
                rout = length_group-1
                while rout < length_formula:
                    find =  True
                    for i in range(length_group):
                        if formula[rout-i] != list_group[length_group-i-1]:
                            find = False
                    if find:
                        molecul_groups.append(group)
                        break
                    if formula[rout] in list(jump.keys()):
                        rout += jump[formula[rout]]
                    else:
                        rout += length_group

        familygroups = []
        for key,value in self.familyandgroup.items():
            for i in range(len(molecul_groups)):
                if molecul_groups[i] == value[0]:
                    familygroups.append([key, value[1]])
                    break
        
        return familygroups

if __name__ == '__main__':
    molecule = GroupsFamily(("carbon_chain", ""))
    print(molecule.identify())