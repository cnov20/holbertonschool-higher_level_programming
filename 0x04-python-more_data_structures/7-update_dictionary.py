def update_dictionary(my_dict, key, value):
        if key and value not in my_dict:
            my_dict[key] = value
        return (my_dict)
