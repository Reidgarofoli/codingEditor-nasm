[BITS 64]
    extern _print

    section   .text
    global _main
_main:
    call      _print                  ; puts(message)
    ret

    section   .data
message:  db        "Hola, mundo", 0        ; C strings need a zero byte at the end