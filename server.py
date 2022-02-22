# student id : M00734701
# importing libraries
import socket
import pickle
from _thread import *
import csv

# initialising the HOST and PORT
HOST ='127.0.0.1'
PORT = 3333



def thread(client_socket):
    try:
        while True:
            # converting csv file into list
            with open('Product.csv', 'r') as product_file:
                content = csv.reader(product_file)
                list_product = list(content)

            # data received from the client side
            list_order = pickle.loads(client_socket.recv(1024))


            # updating the product_file.csv
            with open('Product.csv', 'w', newline='') as updated:
                updated.write('Product_ID,Product_Name,Product_Price,Product_Quantity')
                updated.write('\n')

            with open('Product.csv', 'a', newline='') as updated_file:
                write = csv.writer(updated_file, delimiter=',')

                for product_details in list_product[1:]:
                    for order_details in list_order:
                        if order_details[0] == product_details[1]:
                            new_quantity = int(product_details[3]) - int((order_details[1]))
                            product_details[3] = new_quantity

                    write.writerow(product_details)

            # send message to the client
            client_socket.send('Product Stock updated'.encode())

    except:
        client_socket.close()



def main():
    try:
        # step1- create a server socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            print('Socket successfully created')

            # step2- Bind host and a port with a specific socket
            server_socket.bind((HOST, PORT))

            # step3- Listen for a connection from the client
            server_socket.listen(1)
            print('Waiting for connection')

            while True:
                #step4- Accept requests from a client socket, keeps waiting for incoming connections
                socket_client , (host, port) = server_socket.accept()
                print(f'Received connection from {host} ({port})\n')
                print(f'Connection Established., Connected from: {host}')

                # start a new thread to keep the connection
                start_new_thread(thread, (socket_client,))
    except socket.error as error:
        print(f'Socket creation dropped. Error = {error} ')
        server_socket.close()


main()
