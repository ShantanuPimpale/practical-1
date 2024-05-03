def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Get input from the user
n = int(input("Enter the number of disks: "))
source = input("Enter the source peg: ")
auxiliary = input("Enter the auxiliary peg: ")
destination = input("Enter the destination peg: ")

# Call the tower_of_hanoi function with user input
print("Tower of Hanoi solution:")
tower_of_hanoi(n, source, auxiliary,destination)