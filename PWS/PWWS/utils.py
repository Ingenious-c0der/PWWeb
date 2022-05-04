from dateutil.relativedelta import relativedelta
from pathlib import Path 
import random 
import datetime
import csv
import pandas as pd 
global_done_list = []
global_actual_done_list = []


def get_zone_from_soc_name(name:str,filename:str):
    if name:
         with open(filename) as f:
            data = csv.reader(f)
            for row in data:
                if row[1].lower().strip() == name.lower().strip():
                    return row[3]
    return None

def get_flat_count_from_name(name:str,filename:str):
    if name:
        with open(filename) as f:
            data = csv.reader(f)
            for row in data:
                if row[1].lower().strip() == name.lower().strip():
                    return row[2]
    return None

def are_in_same_area(soc1:str,soc2:str,filename):
    if soc1 and soc2:
        return get_area_from_name(soc1,filename) == get_area_from_name(soc2,filename)
    else:
        return "One of them is none lol"

def get_my_unlucky_pair(unlucky_list,area:str,filename):
    if area:
        for soc in unlucky_list:
            soc_area = get_area_from_name(soc,filename)
            if soc_area == area.lower().strip():
                unlucky_list.remove(soc)
                return soc
    return None

def get_standard_from_name(name:str,filename:str):
    if name:
        classifier_dict = {'East':800,'West':800,'North':1000,'South':800,'Central':800}
        with open(filename) as f:
            data = csv.reader(f)
            for row in data:
                if row[1].lower().strip() == name.lower().strip():
                    try:
                        if int(row[2])>=classifier_dict[row[3]]:
                            return "Angel"
                        elif float(row[-1])<=2500:
                            return "Worst"
                        else:
                            return "Medium"
                    except:
                        pass
    return None

def generate_week_capsules_alternate(zone,filename:str):
    global global_done_list 
    _zone = get_zone(zone,filename)
    _classified = classifier(_zone)
    capsule_holder = []
    done = global_done_list
    angel_dict = group_into_area(_classified[1])
    medium_dict = group_into_area(_classified[3])
    worst_dict = group_into_area(_classified[2])
    #new_dict = group_into_area(_classified[0])
    med_items = list(medium_dict.items())
    #new_items = list(new_dict.items())
    worst_items = list(worst_dict.items())
    angel_items = list(angel_dict.items())
    for i in range(3):
        area_reference = [False,False,False,False,False,False,False]
        week = [[],[],[],[],[],[]]
        for area, soc_list in med_items:
            if len(soc_list)>=2:
                    if not area_reference[0]:
                            area_reference[0] = area
                    for soc in soc_list :
                        if soc[1] not in done and area_reference[0] == area: 
                                week[0].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[0])>=2:
                                break 
                    if len(week[0])>=2:
                        week[0].append(area_reference[0])
                        break




        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[1]:
                            area_reference[1] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[1] == area: 
                                week[1].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[1])>=2:
                                break 
                    if len(week[1])>=2:
                        week[1].append(area_reference[1])
                        break


        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[2] == area: 
                                week[2].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[2])>=2:
                                break 
                    if len(week[2])>=2:
                        week[2].append(area_reference[2])
                        break


        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[3]:
                            area_reference[3] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[3] == area: 
                                week[3].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[3])>=2:
                                break 
                    if len(week[3])>=2:
                        week[3].append(area_reference[3])
                        break

        for area, soc_list in angel_items:
                    if not area_reference[4]:
                            area_reference[4] = area
                    for soc in soc_list :

                        if  area_reference[4] == area: 
                                week[4].append(soc[1])
                                done.append(soc[1])
                                global_done_list.append(soc[1])
                        if len(week[4])>=2:
                                break 
                    if len(week[4])>=2:
                        week[4].append(area_reference[4])
                        break


        random.shuffle(angel_items)
        for area, soc_list in angel_items:
                    if not area_reference[5]:
                            area_reference[5] = area
                    for soc in soc_list :

                        if  area_reference[5] == area and soc[1] not in week[4]: 
                                week[5].append(soc[1])
                                done.append(soc[1])
                                global_done_list.append(soc[1])
                        if len(week[5])>=2:
                                break 
                    if len(week[5])>=2:
                        week[5].append(area_reference[5])
                        break


        #filler
        for day in week:
            if len(day) == 0 :
                area_reference = [False,False,False,False,False,False,False]
                for area, soc_list in med_items:
                    if not area_reference[2] :
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[2] == area: 
                                day.append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(day)>=2:
                                break 
                    if len(day)>=2:
                        day.append(area_reference[2])
                        break



        #checking failures 
        for day_num in range(len(week)):
            if len(week[day_num]) == 0 :
                week[day_num].append(None)
                week[day_num].append(None)
                week[day_num].append(None)

            if len(week[day_num]) == 1 :
                direct_soc = get_direct_soc(done,get_area_from_name(week[day_num][0],filename),day_num==4 or day_num==5,filename)
                week[day_num].append(direct_soc)
                global_done_list.append(direct_soc)
                week[day_num].append(get_area_from_name(week[day_num][0],filename))
        #smart filler 
        for day in week:
            if day.count(None) == 3:
                day[0] = unrestricted_zone_filling(done,zone,filename)
                day[1] = unrestricted_zone_filling(done,zone,filename,get_area_from_name(day[0],filename))
                global_done_list.append(day[0])
                global_done_list.append(day[1])
                try:
                    day[2] = get_area_from_name(day[0])

                except:
                    day[2] = None 





        #utility for clubbing similar areas
        temp_sche_list = [[],[],[],[],[],[]]
        sche_list = week 
        sat_c, sun_c = 0 ,0 
        for day in sche_list:
            if day[2] == sche_list[5][2]:
                sun_c+=1

            if day[2] == sche_list[4][2]:
                sat_c+=1
        if sun_c>sat_c:
            temp = sche_list[5]
            sche_list[5] = sche_list[4]
            sche_list[4] = temp 
        temp_sche_list[5] = sche_list[5]
        temp_sche_list[4] = sche_list[4]

        day_num = 3
        for i in range(-3,-7,-1):
            if sche_list[i][2] == sche_list[4][2]:
                temp_sche_list[day_num] = sche_list[i]
                day_num-=1
        sche_list = [i for i in sche_list if i != temp_sche_list[5] and i[2]!=temp_sche_list[4][2]]
        temp_week = sche_list
        for day in range(len(temp_week[0:day_num+1])):
                    temp_sche_list[day] = sche_list[day]
                    for i in temp_week :
                        if temp_sche_list[day][2] == i[2] and i not in temp_sche_list:
                            temp_sche_list[day+1] = i 

        week = temp_sche_list

        capsule_holder.append(week)

    return capsule_holder

def check_week_capsule_health(week_capsule:list)->str:
    none_day_count = 0 
    for day in week_capsule:
        if day.count(None)==3:
            none_day_count += 1
    if none_day_count >= 2:
        return f"low"
    elif none_day_count == 1:
        return "medium"
    else:
        return "good"

def group_into_area_spec(soc_list:list,filename)->dict:
    area_dict = {}
    for society in soc_list:
        if get_area_from_name(society,filename).lower().strip() not in area_dict.keys():
            area_dict[get_area_from_name(society,filename).lower().strip()] = [society]
        else:
            area_dict[get_area_from_name(society,filename).lower().strip()].append(society)
    return area_dict

def group_into_area(scrambled_soc_lists:tuple)->dict[str:list]:
    area_dict  =  { }
    for society in scrambled_soc_lists:
        if society[4].lower().strip() not in area_dict.keys():
            area_dict[society[4].lower().strip()] = [society]
        else:
            area_dict[society[4].lower().strip()].append(society)
    return area_dict

def get_zone(zone_name:str,filename:str,get_length=False)->list:
    zone_list = []
    repeat_check = {}
    with open(filename) as f:
        data = csv.reader(f)
        for row in data:
            if row[3].lower().strip() == zone_name.lower() and row[1].lower().strip() not in repeat_check.keys() and row[-3].lower().strip() == 'repeat' :
                zone_list.append(row)
                repeat_check[row[1].lower().strip()] = True
    if get_length:
        return len(zone_list)
    else:
        return zone_list

def classifier(zone_list:list)->tuple[tuple,tuple,tuple]:
    """
    new soc should be empty for now 
    """
    new_soc = []
    angel_soc = []
    worst_soc = []
    medium_soc = []
    classifier_dict = {'East':800,'West':800,'North':800,'South':800,'Central':800}
    for society in zone_list:

        if int(society[2])>=classifier_dict[society[3]]:
            angel_soc.append(society)
        elif float(society[-1])<=2500:
            worst_soc.append(society)
        else:
            medium_soc.append(society)

    return tuple([tuple(new_soc), tuple(angel_soc), tuple(worst_soc),tuple( medium_soc)])

def get_area_from_name(name:str,filename:str):
    if name:
        with open(filename) as f:
            data = csv.reader(f)
            for row in data:
                if row[1].lower().strip() == name.lower().strip():
                    return row[4].lower().strip()
    return None

def get_zone_from_area_name(area_name:str,filename:str)->str:
    if area_name == None:
        return None 
    with open(filename) as f:
        data = csv.reader(f)
        for row in data:
            if row[4].lower().strip() == area_name.lower().strip():
                return row[3].lower().strip()
    return "No Zone"

def print_schedule_dict(sc_dict:dict)->None:
    for date,soc_list in sorted(sc_dict.items()):
        print(f' {date} : {soc_list}')

def is_monday(d):
    return d.weekday() == 0

def is_tuesday(d):
    return d.weekday() == 1

def week_full(week:list):
    for i in range(len(week)):
        if len(week[i])<=2:
            return False
    return True
# not in use right now 
def get_day_societies(day_int:int , done_list:list,items_list,week):
    random.shuffle(items_list)
    area_reference = False
    for area, soc_list in items_list:
                    if not area_reference:
                            area_reference = area
                    for soc in soc_list :

                        if soc[1] not in done_list and area_reference == area: 
                                week[day_int].append(soc[1])

                                done_list.append(soc[1])
                        if len(week[day_int])>=2:
                                break 
                    if len(week[day_int])>=2:
                        week[day_int].append(area_reference)
                        break
                    area_reference = False

def get_angel_day_soieties():
    pass 

def get_direct_soc(done_list:list,area:str,angel:bool,filename:str)->str:

    with open(filename) as f:
        data = csv.reader(f)
        if angel:
            for row in data:
                if row[1] not in done_list and row[4].lower().strip() == area.lower().strip() and int(row[2])>=1000:
                    done_list.append(row[1])
                    return row[1]
        #return a society anyway
        for row in data:
            if row[1] not in done_list and row[4].lower().strip() == area.lower().strip():
                done_list.append(row[1])
                return row[1]
    return None

#discouraged to use this function because it bypasses many checks
def unrestricted_zone_filling(done_list,zone,filename:str,area=None):
    with open(filename, 'r') as f:
        data = csv.reader(f)
        for row in data:
            if area:
                if row[1] not in done_list and row[3].lower().strip() == zone.lower().strip() and row[4].lower().strip() == area.lower().strip():
                    done_list.append(row[1])
                    return row[1]

            else:
                if row[1] not in done_list and row[3].lower().strip() == zone.lower().strip():
                    done_list.append(row[1])
                    return row[1]

    return None

def generate_week_capsules(zone:str,filename:str):
    global global_done_list
    _zone = get_zone(zone,filename)

    _classified = classifier(_zone)
    capsule_holder = []
    done = []
    angel_dict = group_into_area(_classified[1])
    medium_dict = group_into_area(_classified[3])
    worst_dict = group_into_area(_classified[2])
    #new_dict = group_into_area(_classified[0])
    med_items = list(medium_dict.items())
    #new_items = list(new_dict.items())
    worst_items = list(worst_dict.items())
    angel_items = list(angel_dict.items())
    for i in range(3):
        area_reference = [False,False,False,False,False,False,False]
        week = [[],[],[],[],[],[]]
        for area, soc_list in med_items:
            if len(soc_list)>=2:
                    if not area_reference[0]:
                            area_reference[0] = area
                    for soc in soc_list :
                        if soc[1] not in done and area_reference[0] == area: 
                                week[0].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[0])>=2:
                                break 
                    if len(week[0])>=2:
                        week[0].append(area_reference[0])
                        break




        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[1]:
                            area_reference[1] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[1] == area: 
                                week[1].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[1])>=2:
                                break 
                    if len(week[1])>=2:
                        week[1].append(area_reference[1])
                        break

        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[2] == area: 
                                week[2].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[2])>=2:
                                break 
                    if len(week[2])>=2:
                        week[2].append(area_reference[2])
                        break

        random.shuffle(med_items)
        for area, soc_list in med_items:
                    if not area_reference[3]:
                            area_reference[3] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[3] == area: 
                                week[3].append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(week[3])>=2:
                                break 
                    if len(week[3])>=2:
                        week[3].append(area_reference[3])
                        break

        for area, soc_list in angel_items:
                    if not area_reference[4]:
                            area_reference[4] = area
                    for soc in soc_list :

                        if  area_reference[4] == area: 
                                week[4].append(soc[1])
                                done.append(soc[1])
                                global_done_list.append(soc[1])
                        if len(week[4])>=2:
                                break 
                    if len(week[4])>=2:
                        week[4].append(area_reference[4])
                        break

        random.shuffle(angel_items)
        for area, soc_list in angel_items:
                    if not area_reference[5]:
                            area_reference[5] = area
                    for soc in soc_list :

                        if  area_reference[5] == area and soc[1] not in week[4]: 
                                week[5].append(soc[1])
                                done.append(soc[1])
                                global_done_list.append(soc[1])
                        if len(week[5])>=2:
                                break 
                    if len(week[5])>=2:
                        week[5].append(area_reference[5])
                        break

        #filler
        for day in week:
            if len(day) == 0 :
                area_reference = [False,False,False,False,False,False,False]
                for area, soc_list in med_items:
                    if not area_reference[2] :
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc[1] not in done and area_reference[2] == area: 
                                day.append(soc[1])
                                global_done_list.append(soc[1])
                                done.append(soc[1])
                        if len(day)>=2:
                                break 
                    if len(day)>=2:
                        day.append(area_reference[2])
                        break

        #checking failures 
        for day_num in range(len(week)):
            if len(week[day_num]) == 0 :
                week[day_num].append(None)
                week[day_num].append(None)
                week[day_num].append(None)

            if len(week[day_num]) == 1 :
                direct_soc = get_direct_soc(done,get_area_from_name(week[day_num][0],filename),day_num==4 or day_num==5,filename)
                week[day_num].append(direct_soc)
                global_done_list.append(direct_soc)
                week[day_num].append(get_area_from_name(week[day_num][0],filename))

        #not so smart filler 
        for day in week:
            if day.count(None) == 3:
                day[0] = unrestricted_zone_filling(done,zone,filename)
                day[1] = unrestricted_zone_filling(done,zone,filename,get_area_from_name(day[0],filename))
                global_done_list.append(day[0])
                global_done_list.append(day[1])
                try:
                    day[2] = get_area_from_name(day[0])

                except:
                    day[2] = None 



        #utility for clubbing similar areas
        temp_sche_list = [[],[],[],[],[],[]]
        sche_list = week 
        sat_c, sun_c = 0 ,0 
        for day in sche_list:
            if day[2] == sche_list[5][2]:
                sun_c+=1

            if day[2] == sche_list[4][2]:
                sat_c+=1
        if sun_c>sat_c:
            temp = sche_list[5]
            sche_list[5] = sche_list[4]
            sche_list[4] = temp 
        temp_sche_list[5] = sche_list[5]
        temp_sche_list[4] = sche_list[4]

        day_num = 3
        for i in range(-3,-7,-1):
            if sche_list[i][2] == sche_list[4][2]:
                temp_sche_list[day_num] = sche_list[i]
                day_num-=1
        sche_list = [i for i in sche_list if i != temp_sche_list[5] and i[2]!=temp_sche_list[4][2]]
        temp_week = sche_list
        for day in range(len(temp_week[0:day_num+1])):
                    temp_sche_list[day] = sche_list[day]
                    for i in temp_week :
                        if temp_sche_list[day][2] == i[2] and i not in temp_sche_list:
                            temp_sche_list[day+1] = i 

        week = temp_sche_list
        capsule_holder.append(week)

    return capsule_holder


def generate_week_capsules_from_dict(area_dict:dict,filename):
    capsule_holder = [ ]
    area_items = list(area_dict.items())
    done = []
    for i in range(3):
        area_reference = [False,False,False,False,False,False,False]
        week = [[],[],[],[],[],[]]
        for area, soc_list in area_items:
            if len(soc_list)>=2:
                    if not area_reference[0]:
                            area_reference[0] = area
                    for soc in soc_list :
                        if soc not in done and area_reference[0] == area: 
                                week[0].append(soc)

                                done.append(soc)
                        if len(week[0])>=2:
                                break 
                    if len(week[0])>=2:
                        week[0].append(area_reference[0])
                        break




        random.shuffle(area_items)
        for area, soc_list in area_items:
                    if not area_reference[1]:
                            area_reference[1] = area
                    for soc in soc_list :

                        if soc not in done and area_reference[1] == area: 
                                week[1].append(soc)

                                done.append(soc)
                        if len(week[1])>=2:
                                break 
                    if len(week[1])>=2:
                        week[1].append(area_reference[1])
                        break

        random.shuffle(area_items)
        for area, soc_list in area_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc not in done and area_reference[2] == area: 
                                week[2].append(soc)

                                done.append(soc)
                        if len(week[2])>=2:
                                break 
                    if len(week[2])>=2:
                        week[2].append(area_reference[2])
                        break

        random.shuffle(area_items)
        for area, soc_list in area_items:
                    if not area_reference[3]:
                            area_reference[3] = area
                    for soc in soc_list :
                        if soc not in done and area_reference[3] == area: 
                                week[3].append(soc)

                                done.append(soc)
                        if len(week[3])>=2:
                                break 
                    if len(week[3])>=2:
                        week[3].append(area_reference[3])
                        break

        for area, soc_list in area_items:
                    if not area_reference[4]:
                            area_reference[4] = area
                    for soc in soc_list :

                        if  area_reference[4] == area: 
                                week[4].append(soc)
                                done.append(soc)
                        if len(week[4])>=2:
                                break 
                    if len(week[4])>=2:
                        week[4].append(area_reference[4])
                        break

        random.shuffle(area_items)
        for area, soc_list in area_items:
                    if not area_reference[5]:
                            area_reference[5] = area
                    for soc in soc_list :
                        if  area_reference[5] == area and soc not in week[4]: 
                                week[5].append(soc)
                                done.append(soc)
                        if len(week[5])>=2:
                                break 
                    if len(week[5])>=2:
                        week[5].append(area_reference[5])
                        break

        #filler
        for day in week:
            if len(day) == 0 :
                area_reference = [False,False,False,False,False,False,False]
                for area, soc_list in area_items:
                    if not area_reference[2] :
                            area_reference[2] = area
                    for soc in soc_list :

                        if soc not in done and area_reference[2] == area: 
                                day.append(soc)
                                done.append(soc)
                        if len(day)>=2:
                                break 
                    if len(day)>=2:
                        day.append(area_reference[2])
                        break

        #checking failures 
        for day_num in range(len(week)):
            if len(week[day_num]) == 0 :
                week[day_num].append(None)
                week[day_num].append(None)
                week[day_num].append(None)

            if len(week[day_num]) == 1 :
                direct_soc = get_direct_soc(done,get_area_from_name(week[day_num][0],filename),day_num==4 or day_num==5,filename)
                week[day_num].append(direct_soc)
                global_done_list.append(direct_soc)
                week[day_num].append(get_area_from_name(week[day_num][0],filename))



        #utility for clubbing similar areas
        temp_sche_list = [[],[],[],[],[],[]]
        sche_list = week 
        sat_c, sun_c = 0 ,0 
        for day in sche_list:
            if day[2] == sche_list[5][2]:
                sun_c+=1

            if day[2] == sche_list[4][2]:
                sat_c+=1
        if sun_c>sat_c:
            temp = sche_list[5]
            sche_list[5] = sche_list[4]
            sche_list[4] = temp 
        temp_sche_list[5] = sche_list[5]
        temp_sche_list[4] = sche_list[4]

        day_num = 3
        for i in range(-3,-7,-1):
            if sche_list[i][2] == sche_list[4][2]:
                temp_sche_list[day_num] = sche_list[i]
                day_num-=1
        sche_list = [i for i in sche_list if i != temp_sche_list[5] and i[2]!=temp_sche_list[4][2]]
        temp_week = sche_list
        for day in range(len(temp_week[0:day_num+1])):
                    temp_sche_list[day] = sche_list[day]
                    for i in temp_week :
                        if temp_sche_list[day][2] == i[2] and i not in temp_sche_list:
                            temp_sche_list[day+1] = i 

        week = temp_sche_list
        capsule_holder.append(week)

    return capsule_holder


def week_number_generator(seed:int,total_weeks:int)->list:
    number_set= set()
    h, m, a = seed,seed,seed
    for i in range(seed,total_weeks):
        if h<total_weeks:
            number_set.add(h)
        if a<total_weeks :
            number_set.add(a)
        if m<total_weeks:
            number_set.add(m)
        h += 30
        a += 5
        m += 15
    number_list = list(number_set)
    number_list.sort()
    return number_list

def lay_schedule_per_zone(start_date,zone_week_numbers,week_capsules,schedule_dict,total_weeks,filename:str,count_check:int):
    if count_check>5:
        return 
    repeat_cycler = []
    z = 0
    for i in range(len(zone_week_numbers)):
        if z==3:
            z = 0
        repeat_cycler.append(z)
        z+=1
    r_c = 0 
    for i in range(len(zone_week_numbers)):
        current_date = start_date + relativedelta(weeks=zone_week_numbers[i])

        while not is_tuesday(current_date):
            current_date += relativedelta(days=1)
        #may cause infinite recursion for low number of societies 
        if check_week_capsule_health(week_capsules[repeat_cycler[r_c]]) == "low":
             #shifting to another zone and waving goodbye to this one
             strong_zones = ['West','North','Central','East','South']
             lay_schedule_per_zone(start_date,week_number_generator(zone_week_numbers[i],total_weeks),generate_week_capsules_alternate(random.choice(strong_zones),filename),schedule_dict,total_weeks,filename,count_check+1)
             return 
        else:
            for j in range(len(week_capsules[repeat_cycler[r_c]])):
                    schedule_dict[f'{current_date:%m-%d-%Y} {zone_week_numbers[i]}'] = week_capsules[repeat_cycler[r_c]][j]
                    current_date += relativedelta(days=1)
        r_c += 1
    


def schedule_generator(start_date: datetime.date, duration_months:int,filename:str):
    #capsules contain the week capsules - 3
    east_capsules = generate_week_capsules('East',filename)
    west_capsules = generate_week_capsules('West',filename)
    south_capsules = generate_week_capsules('South',filename)
    north_capsules = generate_week_capsules('North',filename)
    central_capsules = generate_week_capsules('Central',filename)

    while not is_tuesday(start_date):
        start_date += datetime.timedelta(days=1)
    
    end_date = start_date + relativedelta(months=duration_months)
    total_days = (end_date - start_date).days 

    total_weeks = total_days//7
    schedule_dict = {}
    east_numbers = []
    west_numbers = []
    south_numbers = []
    north_numbers = []
    central_numbers = []
    #assigning week numbers
    seed = 1
    east_numbers = week_number_generator(seed+1,total_weeks)
    west_numbers = week_number_generator(seed,total_weeks)
    south_numbers = week_number_generator(seed+2,total_weeks)
    north_numbers = week_number_generator(seed+3,total_weeks)
    central_numbers = week_number_generator(seed+4,total_weeks)


    lay_schedule_per_zone(start_date,east_numbers,east_capsules,schedule_dict,total_weeks,filename,0)
    lay_schedule_per_zone(start_date,west_numbers,west_capsules,schedule_dict,total_weeks,filename,0)
    lay_schedule_per_zone(start_date,south_numbers,south_capsules,schedule_dict,total_weeks,filename,0)
    lay_schedule_per_zone(start_date,north_numbers,north_capsules,schedule_dict,total_weeks,filename,0)
    lay_schedule_per_zone(start_date,central_numbers,central_capsules,schedule_dict,total_weeks,filename,0)


    return schedule_dict


#final values overriding to prevent Nones 


def extended_func(start_date: datetime.date, end_date:int,filename:str):
        global global_done_list
        global global_actual_done_list
        dict_data = []
        r = relativedelta(start_date, end_date)
        filepath = str(Path(__file__).parent.absolute())+"\csv_files_bay\\"+ filename

        months_difference = (r.years * 12) + r.months
        schedule_dict = schedule_generator(start_date,months_difference,filepath)
        filename_ex = filepath
        for date , soc_list in schedule_dict.items():
            for i in range(2):
                if soc_list[i] not in global_actual_done_list:
                    global_actual_done_list.append(soc_list[i])

        unlucky_soc = []
        for i in global_done_list:
            if i not in global_actual_done_list and i not in unlucky_soc:
                unlucky_soc.append(i)

        for date , soc_list in schedule_dict.items():
            if soc_list[1] == None:
                soc_list[1] = get_my_unlucky_pair(unlucky_soc,soc_list[0],filename_ex)
        schedule_quality = []
        for date , soc_list in schedule_dict.items():
            schedule_quality.append(are_in_same_area(soc_list[0],soc_list[1],filename_ex))
            dict_data.append({'Date':date.split()[0],'Society 1':soc_list[0],'Society 2':soc_list[1],'Area':soc_list[-1],'Zone':get_zone_from_area_name(soc_list[-1],filename_ex),'Week Number':date.split()[1],'Standard':(get_standard_from_name(soc_list[0],filename_ex),get_standard_from_name(soc_list[1],filename_ex)),'Flat Count':(get_flat_count_from_name(soc_list[0],filename_ex),get_flat_count_from_name(soc_list[1],filename_ex))})


        #did not get chance list 
        nope = []
        nope_helper = [ ]
        with open(filepath,'r') as f:
                data = list(csv.reader(f))
                for i in data:
                    soc_name = i[1]
                    if soc_name not in global_actual_done_list and soc_name.lower().strip() not in nope_helper :
                        nope.append({'Date':'To be decided','Society 1':soc_name,'Society 2':soc_name,'Area':i[4],'Zone':i[3],'Week Number':'To be decided','Standard':get_standard_from_name(soc_name,filename_ex),'Flat Count':get_flat_count_from_name(soc_name,filename_ex)})
                        nope_helper.append(soc_name.lower().strip())

        zone_list = [[int(x.split()[-1]),get_zone_from_area_name(y[2],filename_ex)] for x,y in schedule_dict.items()]
        zone_list.sort(key = lambda x:x[0])

        #creating a new csv file for truck 2 input 
        intermidiatefilepath = filepath.split('.')[0] + '_intermediate.csv'
        with open(filepath, 'r') as inp, open(f'{intermidiatefilepath}', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1].lower().strip() in nope_helper:
                    writer.writerow(row)
        df = pd.read_csv(f'{intermidiatefilepath}')
        df.to_csv(f'{intermidiatefilepath}',index=False)
        global_done_list = [ ]
        tc2_schedule_dict = schedule_generator(datetime.date(2022,2,22),4,f'{intermidiatefilepath}')
        filename_ex = f'{intermidiatefilepath}'
        for date , soc_list in tc2_schedule_dict.items():
            for i in range(2):
                if soc_list[i] not in global_actual_done_list:
                    global_actual_done_list.append(soc_list[i])

        unlucky_soc = []
        for i in global_done_list:
            if i not in global_actual_done_list and i not in unlucky_soc:
                unlucky_soc.append(i)

        for date , soc_list in tc2_schedule_dict.items():
            if soc_list[1] == None:
                soc_list[1] = get_my_unlucky_pair(unlucky_soc,soc_list[0],filename_ex)
        schedule_quality = []
        for date , soc_list in tc2_schedule_dict.items():
            schedule_quality.append(are_in_same_area(soc_list[0],soc_list[1],filename_ex))
            dict_data.append({'Date':date.split()[0],'Society 1':soc_list[0],'Society 2':soc_list[1],'Area':get_area_from_name(soc_list[0],filename_ex),'Zone':get_zone_from_soc_name(soc_list[0],filename_ex),'Week Number':date.split()[1],'Standard':(get_standard_from_name(soc_list[0],filename_ex),get_standard_from_name(soc_list[1],filename_ex)),'Flat Count':(get_flat_count_from_name(soc_list[0],filename_ex),get_flat_count_from_name(soc_list[1],filename_ex))})

        dict_data+=nope
        #excel conversion 
        final_csv_path = filepath.split('.')[0] + '_final.csv'
        csv_file_name = f"{final_csv_path}"
        csv_file = csv_file_name
        csv_columns = ['Date','Society 1','Society 2','Area','Zone',"Week Number",'Standard','Flat Count']
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
            return -1

        df_new = pd.read_csv(csv_file_name)
        final_excel_path = str(Path(__file__).parent.absolute())+"\excel_files_bay\\"+filename.split('.')[0]+".xlsx"
        schedule_xlsx = pd.ExcelWriter(f'{final_excel_path}')
        df_new.to_excel(schedule_xlsx, index = False)

        schedule_xlsx.save()
        return final_excel_path







# dict_data = []
# schedule_dict = schedule_generator(datetime.date(2022,2,22),4,"data3.csv")
# filename_ex = 'data3.csv'
# for date , soc_list in schedule_dict.items():
#     for i in range(2):
#         if soc_list[i] not in global_actual_done_list:
#             global_actual_done_list.append(soc_list[i])

# unlucky_soc = []
# for i in global_done_list:
#     if i not in global_actual_done_list and i not in unlucky_soc:
#         unlucky_soc.append(i)

# for date , soc_list in schedule_dict.items():
#     if soc_list[1] == None:
#         soc_list[1] = get_my_unlucky_pair(unlucky_soc,soc_list[0],filename_ex)
# schedule_quality = []
# for date , soc_list in schedule_dict.items():
#     schedule_quality.append(are_in_same_area(soc_list[0],soc_list[1],filename_ex))
#     dict_data.append({'Date':date.split()[0],'Society 1':soc_list[0],'Society 2':soc_list[1],'Area':soc_list[-1],'Zone':get_zone_from_area_name(soc_list[-1],filename_ex),'Week Number':date.split()[1],'Standard':(get_standard_from_name(soc_list[0],filename_ex),get_standard_from_name(soc_list[1],filename_ex)),'Flat Count':(get_flat_count_from_name(soc_list[0],filename_ex),get_flat_count_from_name(soc_list[1],filename_ex))})


# #did not get chance list 
# nope = []
# nope_helper = [ ]
# with open('data3.csv','r') as f:
#         data = list(csv.reader(f))
#         for i in data:
#             soc_name = i[1]
#             if soc_name not in global_actual_done_list and soc_name.lower().strip() not in nope_helper :
#                 nope.append({'Date':'To be decided','Society 1':soc_name,'Society 2':soc_name,'Area':i[4],'Zone':i[3],'Week Number':'To be decided','Standard':get_standard_from_name(soc_name,filename_ex),'Flat Count':get_flat_count_from_name(soc_name,filename_ex)})
#                 nope_helper.append(soc_name.lower().strip())

# zone_list = [[int(x.split()[-1]),get_zone_from_area_name(y[2],filename_ex)] for x,y in schedule_dict.items()]
# zone_list.sort(key = lambda x:x[0])

# #creating a new csv file for truck 2 input 
# with open('data3.csv', 'r') as inp, open('truck2.csv', 'w') as out:
#     writer = csv.writer(out)
#     for row in csv.reader(inp):
#         if row[1].lower().strip() in nope_helper:
#             writer.writerow(row)
# df = pd.read_csv('truck2.csv')
# df.to_csv('truck2.csv',index=False)
# global_done_list = [ ]
# tc2_schedule_dict = schedule_generator(datetime.date(2022,2,22),4,"truck2.csv")
# filename_ex = 'truck2.csv'
# for date , soc_list in tc2_schedule_dict.items():
#     for i in range(2):
#         if soc_list[i] not in global_actual_done_list:
#             global_actual_done_list.append(soc_list[i])

# unlucky_soc = []
# for i in global_done_list:
#     if i not in global_actual_done_list and i not in unlucky_soc:
#         unlucky_soc.append(i)

# for date , soc_list in tc2_schedule_dict.items():
#     if soc_list[1] == None:
#         soc_list[1] = get_my_unlucky_pair(unlucky_soc,soc_list[0],filename_ex)
# schedule_quality = []
# for date , soc_list in tc2_schedule_dict.items():
#     schedule_quality.append(are_in_same_area(soc_list[0],soc_list[1],filename_ex))
#     dict_data.append({'Date':date.split()[0],'Society 1':soc_list[0],'Society 2':soc_list[1],'Area':get_area_from_name(soc_list[0],filename_ex),'Zone':get_zone_from_soc_name(soc_list[0],filename_ex),'Week Number':date.split()[1],'Standard':(get_standard_from_name(soc_list[0],filename_ex),get_standard_from_name(soc_list[1],filename_ex)),'Flat Count':(get_flat_count_from_name(soc_list[0],filename_ex),get_flat_count_from_name(soc_list[1],filename_ex))})




# dict_data+=nope
# #excel conversion 
# csv_file_name = "Scheduletc2.csv"
# csv_file = csv_file_name
# csv_columns = ['Date','Society 1','Society 2','Area','Zone',"Week Number",'Standard','Flat Count']
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dict_data:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")

# df_new = pd.read_csv(csv_file_name)
# schedule_xlsx = pd.ExcelWriter('Scheduletc2.xlsx')
# df_new.to_excel(schedule_xlsx, index = False)

# print(schedule_quality.count(True))
# print(schedule_quality.count("One of them is none lol"))
# print(schedule_quality.count(False))
# schedule_xlsx.save()