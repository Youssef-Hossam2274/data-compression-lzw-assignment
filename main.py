from utils import read_file, write_file, get_string_asci_dictionary, get_asci_string_dictionary


def lzw_compression(data:str): 
    counter = 128
    dictionary = get_string_asci_dictionary()
    data += '$' # dumy char to compress the current_data
    current_data = ''
    compressed_data = ''
    for char in data:
        current_data += char
        if(current_data not in dictionary):
            dictionary[current_data] = counter
            counter += 1
            compressed_data += str(dictionary[current_data[:-1]]) + " "
            current_data = char


    return compressed_data[:-1] # ro remove the last space

def lzw_decompression(data_compressed:str):
    counter = 128
    dictionary = get_asci_string_dictionary()
    encoded_data = data_compressed.split(" ")
    lastData = dictionary[int(encoded_data[0])]
    res = dictionary[int(encoded_data[0])]

    for encode_number in encoded_data[1:]: 
        key = int(encode_number)
        
        current_data = ""
        if(key in dictionary):
            current_data = dictionary[key]
            dictionary[counter] = lastData + current_data[0]
        else:
            current_data = lastData + lastData[0]
            dictionary[counter] = current_data 

        lastData = current_data
        counter += 1
        res += current_data

    return res


def main():
    data = read_file("input.txt")
    data_compressed = lzw_compression(data)
    write_file("output.txt",data_compressed)
    uncompressed_data = lzw_decompression(data_compressed)
    
    if(uncompressed_data == data):
        print("data compression done successfully")
    else:
        print("data compression fail !")


main()