import os

def get_departments():
    with open("appReq/departments/department_names.txt",'r') as dep_file_local:
        department_local = dep_file_local.readlines()
        department_local = [i.strip() for i in department_local]
    return department_local


def get_shot_list():
    with open("appReq/shotList/shot_list.txt",'r') as shot_file_local:
        shot_list_local = shot_file_local.readlines()
        shot_list_local = [i.strip() for i in shot_list_local]
    return shot_list_local


def get_animation_folders():
    with open("appReq/departments/Animation.txt", 'r') as anim_file_local:
        anim_list_local = anim_file_local.readlines()
        anim_list_local = [i.strip() for i in anim_list_local]
    return anim_list_local


def get_matchmove_folders():
    with open("appReq/departments/Matchmove.txt", 'r') as mm_file_local:
        mm_list_local = mm_file_local.readlines()
        mm_list_local = [i.strip() for i in mm_list_local]
    return mm_list_local


def get_mm_equaliser_folders():
    with open("appReq/departments/Matchmove_sub_Equalizer.txt", 'r') as equaliser_file_local:
        equaliser_list_local = equaliser_file_local.readlines()
        equaliser_list_local = [i.strip() for i in equaliser_list_local]
    return equaliser_list_local


def get_rigging_folders():
    with open("appReq/departments/Rigging.txt", 'r') as rigging_file_local:
        rigging_list_local = rigging_file_local.readlines()
        rigging_list_local = [i.strip() for i in rigging_list_local]
    return rigging_list_local



show_name = input("Enter the show name: ")
server_dir = "T:" + "\\"                                                                             #This is the server directory.
show_dir = os.path.join(server_dir,show_name)



cg_shots = []

for i in os.listdir(show_dir):                                                                     # This piece of code is to be executed for MAHA.
                                                                                                   # For shows that have reel or double sub folder system.
    shots_dir = os.path.join(show_dir, i)
    for c in os.listdir(shots_dir):
        shot_dir = os.path.join(shots_dir,c)
        for i in get_shot_list():
            if shot_dir.endswith(i):
                shot_dir = shot_dir + r"\cg"
                cg_shots.append(shot_dir)
            else:
                pass
#
#
#
# for i in os.listdir(show_dir):                                                                # This is for shows that have single folder system, no sub-folders.
#     for shots in get_shot_list():                                                             # This is very fast.
#         if shots == i:
#             shot_path = os.path.join(show_dir,shots,'cg')
#             cg_shots.append(shot_path)



# for root, directory, files in os.walk(show_dir):                                                   # This is for all shows, but it is bit time consuming.
#     if "cg" in directory:
#         for i in get_shot_list():
#             if root.endswith(i):
#                 shot_abs_path = os.path.join(root,'cg')
#                 cg_shots.append(shot_abs_path)



shot_display = []

for i in cg_shots:
    i = i.strip(r"\\cg")
    shot_display.append(os.path.basename(i))

print("These are shots that will have the Folder Structure.")
for i in shot_display:
    print(i)

confirm_message = input("Shots confirmed('yes' or 'no'): ").lower()

if confirm_message == 'yes':


    for i in cg_shots:
        folder_dir = i

        for i in get_departments():
            departments_name = i
            department_dir = os.path.join(folder_dir,i)

            os.mkdir(department_dir)

            if departments_name == "Animation":
                folder_list = get_animation_folders()

                for i in folder_list:
                    anim_folder_name = i
                    anim_folder_dir = os.path.join(department_dir,i)
                    os.mkdir(anim_folder_dir)


            elif departments_name == "Matchmove":
                folder_list = get_matchmove_folders()

                for i in folder_list:
                    mm_folder_name = i
                    mm_folder_dir = os.path.join(department_dir,i)
                    os.mkdir(mm_folder_dir)

                    if mm_folder_name == "Equaliser":
                        folder_list = get_mm_equaliser_folders()
                        for i in folder_list:
                            equaliser_folder_name = i
                            equaliser_folder_dir = os.path.join(mm_folder_dir, i)
                            os.mkdir(equaliser_folder_dir)

                    elif mm_folder_name == "Publish":
                        publish_folder_name = "v001"
                        publish_folder_dir = os.path.join(mm_folder_dir,publish_folder_name)
                        os.mkdir(publish_folder_dir)


                        publish_folder_items = ["Cam","Geo"]
                        for i in publish_folder_items:
                            publish_folder_item_dir = os.path.join(publish_folder_dir,i)
                            os.mkdir(publish_folder_item_dir)


            elif departments_name == "Rigging":
                folder_list = get_rigging_folders()

                for i in folder_list:
                    rig_folder_name = i
                    rig_folder_dir = os.path.join(department_dir,i)
                    os.mkdir(rig_folder_dir)



            else:
                pass

    print("Folder Structure is created.")

else:
    exit()

