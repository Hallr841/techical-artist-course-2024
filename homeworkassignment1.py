import math 

def vector_length(vector):
    #Calculate the sum of the squares of ead component
    sum_of_squares=sum(comp ** 2 for comp in vector)

    # Calculate the Square root of the sum of Squares
    length = math.sqrt(sum_of_squares)

    return length 

def  main():
    vectors = [(3,5.23,2.1532),(1,2,3)] #list of inputs

    for vector in vectors:
        length = vector_length(vector)
        print(f" the length of the vector{vector}is{length}")

if __name__=="__main__":
    main()