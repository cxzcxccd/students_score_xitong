import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json

#定义学生类
class student:
    def __init__(self,name,score,stnum):
        self.name=name
        self.score=score
        self.stnum=stnum


class GUI:
#初始化GUI的各种成员变量：
    def __init__(self):
        self.root = tk.Tk()
        #定义学生列表
        self.students = []
        self.add_image()
        self.load_data()
        ##定义基础四个按钮增删查找
        self.btn1=tk.Button(self.root)
        self.btn2=tk.Button(self.root)
        self.btn3 = tk.Button(self.root)
        self.btn4 = tk.Button(self.root)
        self.btn5=tk.Button(self.root)
        self.btn6=tk.Button(self.root)
        self.btn1["text"]="添加"
        self.btn2["text"] = "查找"
        self.btn3["text"] = "删除"
        self.btn4["text"] = "显示"
        self.btn5["text"]="排序"
        self.btn6["text"]="保存"
        self.root.geometry("800x1000+1100+150")
        self.btn1.bind("<Button-1>", self.add)
        self.btn2.bind("<Button-1>", self.find)
        self.btn3.bind("<Button-1>", self.delete)
        self.btn4.bind("<Button-1>", self.show)
        self.btn5.bind("<Button-1>",self.Sort)
        self.btn6.bind("<Button-1>",self.save)
        self.btn1.place(relx=0, x=0, y=300, relwidth=0.1, relheight=0.1)
        self.btn2.place(relx=0, x=0, y=400, relwidth=0.1, relheight=0.1)
        self.btn3.place(relx=0, x=0, y=500, relwidth=0.1, relheight=0.1)
        self.btn4.place(relx=0, x=0, y=600, relwidth=0.1, relheight=0.1)
        self.btn5.place(relx=0, x=0, y=700, relwidth=0.1, relheight=0.1)
        self.btn6.place(relx=0, x=0, y=800, relwidth=0.1, relheight=0.1)



    def add(self, event):
        name = simpledialog.askstring("添加学生", "请输入学生姓名：")
        if name:
            score = simpledialog.askinteger("添加学生", "请输入学生分数：")
            if score is not None:
                stnum = simpledialog.askstring("添加学生", "请输入学生学号：")
                if stnum:
                    new_student = student(name, score, stnum)
                    self.students.append(new_student)
                    messagebox.showinfo("成功", "学生添加成功。")
    def find(self,event):
      option = simpledialog.askstring("查找学生", "请选择查找方式（学号/姓名/成绩）：")
      findstnum=None
      findscore=None
      findname=None
      if option == "学号":
          findstnum=simpledialog.askstring("待查学号","请输入待查学号")
          t=None
          for student in self.students:
              if student.stnum==findstnum:
                  t=1
                  student_info = " "
                  student_info += f"姓名：{student.name},分数: {student.score}, 学号: {student.stnum}\n"
                  break
          if t:
            messagebox.showinfo("找到了", student_info)
          else :
              messagebox.showinfo("没找到","您输入的学号没有对应的学生哦")

      elif option=="姓名":
          findname=simpledialog.askstring("待查姓名","请输入待查姓名")
          found_students = [student for student in self.students if student.name == findname]
          if found_students:
              student_info = ""
              for student in found_students:
                  student_info += f"姓名：{student.name}, 分数：{student.score}, 学号：{student.stnum}\n"
              messagebox.showinfo("找到了", student_info)
          else:
              messagebox.showinfo("没找到", f"您输入的{option}没有对应的学生哦。")

      elif option=="成绩":
          findscore = simpledialog.askinteger("待查成绩", "请输入待查成绩")
          found_students = [student for student in self.students if student.score == findscore]
          if found_students:
              student_info = ""
              for student in found_students:
                  student_info += f"姓名：{student.name}, 分数：{student.score}, 学号：{student.stnum}\n"
              messagebox.showinfo("找到了", student_info)
          else:
              messagebox.showinfo("没找到", f"您输入的{option}没有对应的学生哦。")
      else :
          messagebox.showinfo("fail", "您查找的方式有问题哦.")






    def Sort(self, event):
        option = simpledialog.askstring("排序学生", "请选择排序方式（学号/成绩）：")
        if option == "学号":
            self.students.sort(key=lambda student: student.stnum)
            messagebox.showinfo("排序完成", "按照学号排序完成。")
        elif option == "成绩":
            self.students.sort(key=lambda student: student.score)
            messagebox.showinfo("排序完成", "按照成绩排序完成。")
        else:
            messagebox.showinfo("失败", "您选择的排序方式有问题哦。")

        # 输出排序后的学生列表
        self.show(None)

    def delete(self, event):
            # 以三种方式删除
            option = simpledialog.askstring("删除学生", "请选择删除方式（学号/姓名/成绩）：")
            if option == "学号":
                findstnum = simpledialog.askstring("待删学号", "请输入待删除学生的学号：")
                deleted_students = [student for student in self.students if student.stnum == findstnum]
                if deleted_students:
                    for student in deleted_students:
                        self.students.remove(student)
                    messagebox.showinfo("删除成功", f"已成功删除{len(deleted_students)}位学生。")
                else:
                    messagebox.showinfo("删除失败", "未找到对应学号的学生。")
            elif option == "姓名":
                findname = simpledialog.askstring("待删姓名", "请输入待删除学生的姓名：")
                deleted_students = [student for student in self.students if student.name == findname]
                if deleted_students:
                    for student in deleted_students:
                        self.students.remove(student)
                    messagebox.showinfo("删除成功", f"已成功删除{len(deleted_students)}位学生。")
                else:
                    messagebox.showinfo("删除失败", "未找到对应姓名的学生。")
            elif option == "成绩":
                findscore = simpledialog.askinteger("待删成绩", "请输入待删除学生的成绩：")
                deleted_students = [student for student in self.students if student.score == findscore]
                if deleted_students:
                    for student in deleted_students:
                        self.students.remove(student)
                    messagebox.showinfo("删除成功", f"已成功删除{len(deleted_students)}位学生。")
                else:
                    messagebox.showinfo("删除失败", "未找到对应成绩的学生。")
            else:
                messagebox.showinfo("删除失败", "您选择的删除方式有问题哦。")

            # 输出删除后的学生列表
            self.show(None)





    def show(self, event):
        if len(self.students)==0:
            messagebox.showinfo("没有学生","没有学生记录")
        else :
            student_info=" "
        for student in self.students:
            student_info+=f"姓名：{student.name},分数: {student.score}, 学号: {student.stnum}\n"
        messagebox.showinfo("学生列表", student_info)

    def save(self, event):
        try:
            with open('students.json', 'w') as file:
                data = [{'name': student.name, 'score': student.score, 'stnum': student.stnum} for student in
                        self.students]
                json.dump(data, file)
            messagebox.showinfo("保存成功", "学生数据已成功保存到文件。")
        except Exception as e:
            messagebox.showinfo("保存失败", f"保存学生数据时出现错误：{str(e)}")

    def    load_data(self):

      try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            for item in data:
                name = item['name']
                score = item['score']
                stnum = item['stnum']
                sb = student(name, score, stnum)
                self.students.append(sb)
      except Exception as e:
          messagebox.showinfo("数据加载失败", f"加载学生数据时出现错误：{str(e)}")


    def Run(self):
        self.root.title("学生成绩管理系统")
        self.root.mainloop()
    def add_image(self):
      image_path = "河师大校徽.png"
      self.image = tk.PhotoImage(file=image_path)
      label = tk.Label(self.root, image=self.image)
      label.place(relx=0, rely=0, anchor="nw")







if __name__ == '__main__':
    a = GUI()
    a.Run()
