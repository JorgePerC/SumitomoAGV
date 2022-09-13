#include <stdio.h>
#include <linux/can.h>
#include <linux/types.h>
// #include <linux/socket.h>
#include <sys/socket.h>

//#include "CANopen.h"
//#include "storage/CO_storage.h"

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#include <iostream>

int main(int argc, char const *argv[]){
    CO_t *co;
    int s = socket(PF_CAN, SOCK_RAW, CAN_RAW);

    std::cout << "Hola mundo" << std::endl;

    return 0;
}
