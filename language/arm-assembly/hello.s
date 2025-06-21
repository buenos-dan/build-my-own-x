.global _start

.data
msg:
    .asciz "Hello, world!\n"

.text
_start:
    B _print_hello
    MOV     R5, #11
    B _print_number

    MOV     R0, #0         
    MOV     R7, #1        
    SWI     #0           

_print_hello:
    MOV     R0, #1              
    LDR     R1, =msg           
    MOV     R2, #14           
    MOV     R7, #4           
    SWI     #0              

    B _start+4

_print_number:
    MOV     R0, #1              
    MOV     R1, R2           
    MOV     R2, #4           
    MOV     R7, #4           
    SWI     #0              

    B _start+12

