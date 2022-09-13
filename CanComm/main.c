
#include <linux/can.h>
#include <iostream>

// You probably need to install libsocketcan

int main(int argc, char const *argv[])
{
    /* code */
    std::cout << "hola" << std::endl;

    // Create a socket

    s = socket(PF_CAN, SOCK_RAW, CAN_RAW);

    return 0;
}
