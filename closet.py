import tkinter as tk

def clear_entry(entry):
    entry.delete(0, tk.END)
       
root = tk.Tk()
root.geometry("400x600")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


canvas.create_line(0, 20, 400, 20, width=2)
canvas.create_text(15, 10, text="1", font=("Arial", 15, "bold"))
canvas.create_line(15, 20, 15, 100, width=2)

canvas.create_text(105, 10, text="2", font=("Arial", 15, "bold"))
canvas.create_line(105, 20, 105, 100, width=2)

canvas.create_text(195, 10, text="3", font=("Arial", 15, "bold"))
canvas.create_line(195, 20, 195, 100, width=2)

canvas.create_text(285, 10, text="4", font=("Arial", 15, "bold"))
canvas.create_line(285, 20, 285, 100, width=2)

canvas.create_text(375, 10, text="5", font=("Arial", 15, "bold"))
canvas.create_line(375, 20, 375, 100, width=2)

red_rectangle = canvas.create_rectangle(1, 100, 31, 200, fill="red")
yellow_rectangle = canvas.create_rectangle(91, 100, 121, 200, fill="yellow")
green_rectangle = canvas.create_rectangle(181, 100, 211, 200, fill="green")
blue_rectangle = canvas.create_rectangle(271, 100, 301, 200, fill="blue")
purple_rectangle = canvas.create_rectangle(361, 100, 391, 200, fill="purple")

canvas_list = [red_rectangle, yellow_rectangle, green_rectangle, blue_rectangle, purple_rectangle]

rectangle_dict = {"1":red_rectangle, "2":yellow_rectangle, "3":green_rectangle, "4":blue_rectangle, "5":purple_rectangle}
temp_rect = dict(rectangle_dict)   
color_dict = {"1":"red", "2":"yellow", "3":"green", "4":"blue", "5":"purple"}
temp_color = dict(color_dict)
# part 1
color1_entry = tk.Entry(root)
color1_entry.insert(0, "Input the number")
color1_entry.bind("<Button-1>", lambda event: clear_entry(color1_entry))

color2_entry = tk.Entry(root)
color2_entry.insert(0, "Input the number")
color2_entry.bind("<Button-1>", lambda event: clear_entry(color2_entry))

color1_entry.place(x=0, y=300)
color2_entry.place(x=0, y=330)

# part 2
cloth_entry = tk.Entry(root)
cloth_entry.insert(0, "Input the number")
cloth_entry.bind("<Button-1>", lambda event: clear_entry(cloth_entry))

cloth_entry.place(x=0, y=400)

# part 3
cloth_input_entry = tk.Entry(root)
cloth_input_entry.insert(0, "Input the location")
cloth_input_entry.bind("<Button-1>", lambda event: clear_entry(cloth_input_entry))
cloth_input_entry.place(x=0, y=500)

color_input_entry = tk.Entry(root)
color_input_entry.insert(0, "Input the color")
color_input_entry.bind("<Button-1>", lambda event: clear_entry(color_input_entry))
color_input_entry.place(x=0, y=530)


def get_input_colors():
    global rectangle_dict, color_dict
    
    color1 = color1_entry.get()
    color2 = color2_entry.get()
    
    if color1 in rectangle_dict and color2 in rectangle_dict:
        temp = canvas.coords(rectangle_dict[color1])
        temp1 = rectangle_dict[color1]
        
        canvas.coords(rectangle_dict[color1], canvas.coords(rectangle_dict[color2]))
        canvas.coords(rectangle_dict[color2],temp)
        
        temp2 = canvas.coords(color_dict[color1])
        temp22 = color_dict[color1]
        
        canvas.coords(color_dict[color1], canvas.coords(color_dict[color2]))
        canvas.coords(color_dict[color2],temp2)
    
        rectangle_dict[color1] = rectangle_dict[color2]
        rectangle_dict[color2] = temp1
        
        color_dict[color1] = color_dict[color2]
        color_dict[color2] = temp22

takes = []
    
def get_the_clothes():
    global rectangle_dict, color_dict
    
    take = cloth_entry.get()
    if take == "all":
        for pick in canvas_list:
            canvas.delete(pick)
    else:
        if take in rectangle_dict and take in color_dict:
            takes.append((rectangle_dict[take],color_dict[take]))
            canvas.delete(rectangle_dict[take])
            rectangle_dict.pop(take)
            color_dict.pop(take)
            print("I have :", takes)
    
def sort_the_clothes():
    global rectangle_dict, color_dict
    sorted_dict = dict(sorted(rectangle_dict.items()))

    index = 1
    for key, value in sorted_dict.items():
        canvas.coords(rectangle_dict[key], index, 100, index + 30, 200)
        canvas.coords(color_dict[key], index, 100, index + 30, 200)
        index += 90
        
    new_rectangle_dict = {}
    new_color_dict = {}
    
    for index, values in enumerate(sorted(rectangle_dict.keys())):
        new_key = str(index + 1)
        new_rectangle_dict[new_key] = rectangle_dict[values]
        new_color_dict[new_key] = color_dict[values]
        
    rectangle_dict.clear()
    color_dict.clear()

    
    for index, values in enumerate(sorted(new_rectangle_dict.keys())):
        new_key = str(index + 1)      
        rectangle_dict[new_key] = new_rectangle_dict[values]
        color_dict[new_key] = new_color_dict[values]      
    new_rectangle_dict.clear()
    new_color_dict.clear()
    
def insert_the_cloth():
    global rectangle_dict, color_dict
    try:
        locate = cloth_input_entry.get()
        cloth_color = color_input_entry.get()
        if len(rectangle_dict) <= 5:
            loc = (int(locate) - 1) * 90 + 1
            temp = canvas.create_rectangle(loc, 100, loc + 30, 200, fill=f"{cloth_color}")
            rectangle_dict[locate] = temp
            color_dict[locate] = cloth_color  
            print(len(rectangle_dict))
            
    except:
        full_lbl = tk.Label(root, text="It's Full !", font=("Helvetica", 24),fg="red", bg="white")
        full_lbl.place(x=150, y=480)
        full_lbl.after(2000,full_lbl.destroy)  
    
part1_lbl = tk.Label(root, text="Part 1")
part1_lbl.place(x=0, y=270)
get_colors_button = tk.Button(root, text="Get Colors", width=10, command=get_input_colors)
get_colors_button.place(x=150, y=330)

part2_lbl = tk.Label(root, text="Part 2")
part2_lbl.place(x=0, y=370)
get_clothes_button = tk.Button(root, text="Get a cloth", width=10, command=get_the_clothes)
get_clothes_button.place(x=150, y=400)
sort_clothes_button = tk.Button(root, text="sort the clothes", width=12, command=sort_the_clothes)
sort_clothes_button.place(x=150, y=430)


part3_lbl = tk.Label(root, text="Part 3")
part3_lbl.place(x=0, y=470)
insert_button = tk.Button(root, text="Insert", width=10, command=insert_the_cloth)
insert_button.place(x=150, y=530)



root.mainloop()