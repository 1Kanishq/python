class clg:
    cname='KEC'
    cloc='Ghaziabad'
    cboard='state'

    def __init__(self,name,rollno,branch,YOP):
        self.name = name
        self.rollno= rollno
        self.branch= branch
        self.YOP= YOP
    
    def disp_obj(self):
        print('name',self.name)
        print('rollno',self.rollno)
        print('branch',self.branch)
        print('YOP',self.YOP)
    
    @classmethod
    # def disp cls(cls):