# Pear Programming Language (v2.0.0)

## Introduction

This language is written by me using python. This Language is using intrepreter. All components (Lexer , Parser , Runtime) is written by me. In this language i have tried to reduce the complexity of the code and tried to implement the syntax similar to the psuedo code so its easier to build a code by just looking at the algorithm. Currently supporting String , int , float , boolean data types. Still in the experimental stage 

## Installation
Installing Pear to your windows operating system is fairly easy.

1) First Download the latest version of pear from our [official github repository](https://github.com/NaveenDanj/pear-v2/releases).
2) Exctract the pear binary to the root of the C drive.
3) Add Pear binary file path to your environment variable.


### Run Pear script
```
Simply run the command 'pear filename.pr'
```

# Examples

## Find maximum number

```
@start

var float n1 = float( input('Enter number 1 : ') )
var float n2 = float( input('Enter number 2 : ') )
var float n3 = float( input('Enter number 3 : ') )

if var['n1'] > var['n2']

    if var['n1'] > var['n3']
        print 'max number is : ' + str( var['n1'] )
    else
        print 'max number is : ' + str( var['n3'] )
    endif

else

    if var['n2'] > var['n3']

        if var['n2'] > var['n1']
            print 'max number is : ' + str( var['n2'] ) 

        else
            print 'max number is : ' + str( var['n1'] ) 
        endif

    else

        if var['n3'] > var['n1']
            print 'max number is : ' + str( var['n3'] ) 

        else
            print 'max number is : ' + str( var['n1'] ) 
        endif

    endif

endif

@end

```

## Factorial of a given number

```

@start

var int n = int( input('Enter number 1 : ') )
var int total = 1

while var['n'] > 0
    set var['total'] = var['total'] * var['n']
    set var['n'] = var['n'] - 1
endwhile

print 'Factorial is ' + str(var['total'])

@end

```