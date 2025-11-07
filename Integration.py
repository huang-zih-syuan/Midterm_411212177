# initial environment
# import modules
import tkinter as tk
import sqlite3
import tkinter.messagebox as messagebox 

# basic GUI 
root = tk.Tk()
root.title('INTEGRATION')
root.geometry('300x400')

# new label and inpu
# student ID label and entry
label_id = tk.Label(root, text='Student ID')
label_id.pack(pady=(15,5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

# student name label and entry
label_name = tk.Label(root, text='Student Name')
label_name.pack(pady=(10,5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

# setting print_student function
def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()

    print ('Student ID: {}'.format(student_id))
    print ('Student Name: {}'.format(student_name))
    print ('-'*30)

# new a button: Print
botton_print = tk.Button(root, text='Print', command=print_student)
botton_print.pack(pady=15)

# connect to database and build environment
conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

# def a create_student()
def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower() # application layer

    cursor.execute('INSERT INTO DB_student (db_student_id, db_student_name) VALUES(?,?)', (student_id, student_name))
    conn.commit()

    print ('Student ID: {}'.format(student_id))
    print ('Student Name: {}'.format(student_name))
    print ('-' * 30)

button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=20)

# ----- NEW: delete by db_student_id -----
def delete_student():
    sid = entry_id.get().strip()
    if not sid:
        messagebox.showwarning("Warning", "請輸入 Student ID")
        return

    # (可選) 再次確認
    # if not messagebox.askyesno("確認刪除", f"確定刪除 db_student_id = {sid} 嗎？"):
    #     return

    try:
        # 先檢查是否存在
        cursor.execute('SELECT COUNT(*) FROM DB_student WHERE db_student_id = ?', (sid,))
        count = cursor.fetchone()[0]

        if count == 0:
            messagebox.showinfo("Info", f"查無 db_student_id = {sid} 的資料")
            return

        # 刪除
        cursor.execute('DELETE FROM DB_student WHERE db_student_id = ?', (sid,))
        conn.commit()
        messagebox.showinfo("Success", f"已刪除 db_student_id = {sid} 的資料")

        # 清空輸入框（可選）
        # entry_id.delete(0, tk.END)
        # entry_name.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# NEW: Delete 按鈕
button_delete = tk.Button(root, text='Delete', command=delete_student)
button_delete.pack(pady=10)

# def a overview_student()
# show all records in sqlite
def overview_student():
    cursor.execute('SELECT * from DB_student')
    overview = cursor.fetchall()
    print (overview)

# new botton Overview
botton_overview = tk.Button(root, text='Overview', command=overview_student)
botton_overview.pack(pady=25)

root.mainloop() #must be put to the end of programming code