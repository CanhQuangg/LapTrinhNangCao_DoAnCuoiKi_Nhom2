# def frame_treeview_data(self, sheet_name, treeview, searchData):
#
#     self.clean_data(treeview)
#
#     self.df = pd.read_excel("Database.xlsx", sheet_name=sheet_name)
#
#     treeview["column"] = list(self.df.columns)
#     treeview["show"] = "headings"
#
#     for column in treeview["columns"]:
#         treeview.heading(column, text=column)
#
#     self.df_rows = self.df.to_numpy().tolist()
#     for row in self.df_rows:
#         treeview.insert("", "end", values=row)

class MyOtherClass:

    @staticmethod
    def method(arg):
        print(arg)


my_other_object = MyOtherClass()
my_other_object.method("foo")