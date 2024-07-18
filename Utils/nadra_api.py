def search_cnic(file_name, cnic_num):
    try:
        with open(file_name,'r') as file:

            lines = file.readlines()

            for line in lines:

                data = line.strip().split(',')

                if len(data)==5:
                    cnic, name, age, ph_num, address = data
                    
                    if cnic.strip()== cnic_num:
                        return name.strip(), age.strip(), ph_num.strip(), address.strip()
        return None, None, None, None
    
    except FileNotFoundError:
        
        print(f"The file {file_name} does not exist.")
        return None, None, None, None   
def main():
    cnic_num = input( " Enter CNIC Number of the Citizen:")
    file_name = 'citizens_data.txt'

    name, age, ph_num, address = search_cnic(file_name, cnic_num);

    if name and age and ph_num and address:
        print(f" Name:{name}\n Age:{age}\n Phone Number: {ph_num} \n Address:{address}")
    else:
        print("CNIC number not found.")

if __name__ == "__main__":
    main()