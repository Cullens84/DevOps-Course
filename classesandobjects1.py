class results:
    # class name
    name = ""
    physics = 0
    chemistry = 0

    def assignmarks(self, na, phy, che):
        self.name = na
        self.physics = phy
        self.chemistry = che
    # a function calling the seperate datasets

    def showresults(self):
        total = self.physics+self.chemistry
        percentage = total*100/300
        print("name of the student", self.name)
        print("total marks:", total)
        print("percentage:", percentage)
# a function to add the two marks of physics and chemistry, times by 100 divide by 300and print the results
# the .self markers are assigned to order the calls in the code and reference each one seperate


# function or method within the class
students1 = results()
students1.assignmarks("shafeeq", 90, 60)
students1.showresults()
# these calls for the functions within the objects are like filepaths to instances to create the function execute it save it and move on
students2 = results()
students2.assignmarks("james", 99, 78)
students2.showresults()
# both calls are seperated so the second one does not erase the first one
