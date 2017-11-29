## Create a function called draw_stars() that takes a list of numbers and prints out *.##

x = [12,5,3,24,9,17]                            ## sets our list to be called inside the function ##

def draw_stars(x, var):                         ## starts our function "draw_stars" and sets the parameter between x (name of the list) and var
    
    b=[]                                        ## sets a new list to be used later

    for i in x:                                 ## Calls each value in the list of x - I.E. [12,5,3,24]##

        i = i*var                               ## i is equal to i multiplied to the value of var##

        b.append(i)                             ## insert i into the "b" list##

    return b                                    ##return b##

for i in draw_stars (x, "*"): 

    print i                                     ##prints i##
    

## Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. ##

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]       ## sets up our list for our function ##

def draw_stars2(my_list):                               ## names our function and that we want to solve for my list##

    for item in my_list:                                ## 

        output = ''                                     ## sets up an empty variable called output ##

        if type(item) is int:                           ## if the type of item is an integer ##

            for i in range(item):

                output += '*'                           ## add a * to the output ##

        elif type(item) is str:                         ## if the type of item is a string ##

            first_letter = item[0].lower()              ##

            for i in range(len(item)):                  ##
            
                output += first_letter                  ## add the first_letter of the item to outout
        
        print output                                    ## print output

draw_stars2(y)






########################################################
def stars(list):
        for i in range(len(list)):
            print '*'*list[i]

stars ([4,6,1,3,5,25])

########################################################
def stars2(arr):
    for thing in arr:
        if type(thing) is int:
            print '*'*thing
        elif type(thing) is str:
            print thing[0].lower()*len(thing)

stars2([4, "Tom",1,"'Michael",5,7,"Jimmy"])
