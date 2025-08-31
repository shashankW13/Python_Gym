def cli_analytics_tool():
    import pandas as pd
    import os
    import seaborn as sns
    import matplotlib.pyplot as plt

    numeric_columns = ['Sales', 'Profit', 'Quantity', 'Discount']

    def load_csv():
        df_data_dict = {}
        print("\n")
        print("Upload your data".center(40, '='))

        #Loading CSV file
        file_name = input("Add the name of the CSV file you want to analyse: ").strip()

        try:
            script_dir = os.path.dirname(__file__)  # folder where this .py file is
            file_path = os.path.join(script_dir, f"{file_name}.csv")
            csv_data = pd.read_csv(file_path)
            
            df = pd.DataFrame(csv_data)
            df_data_dict['file_name'] = file_name
            df_data_dict['df'] = df
            df_data_dict['numeric_columns_sum'] = df[numeric_columns].sum().to_dict()
            df_data_dict['numeric_columns_average'] = df[numeric_columns].mean().to_dict()
            df_data_dict['numeric_columns_min'] = df[numeric_columns].min().to_dict()
            df_data_dict['numeric_columns_max'] = df[numeric_columns].max().to_dict()
            df_data_dict['numeric_columns_count'] = df[numeric_columns].count().to_dict()
            
            print(f"'{file_name}.csv' found!\nData uploaded successfully!\n")
            return df_data_dict
        
        except FileNotFoundError as f:
            print(f"'{file_name}.csv' file not found!")
            return 0

    #Preview Data
    def preview_data(df):
        continue_preview = 'y'
        while continue_preview == 'y':
            print("\n")
            print("PREVIEW DATA".center(40, '='))
            print("1.Total rows")
            print("2.Column headers")
            print("3.Display first number of rows")

            try:
                preview_choice = int(input("Enter your choice (1-3): "))
            except ValueError:
                print("Enter numerical choices!")

            if preview_choice == 1:
                print(f"Total rows in {df_dict['file_name']}.csv: {len(df)}\n")
                continue_preview = input("Stay on this menu (y/n)?: ")
                 
            elif preview_choice == 2:
                print(f"\nColumn headers in {df_dict['file_name']}.csv: {df.columns}\n")
                continue_preview = input("Stay on this menu (y/n)?: ")
            
            elif preview_choice == 3:
                print(f"\nFirst 15 rows in {df_dict['file_name']}.csv: {df.head(15)}\n")
                continue_preview = input("Stay on this menu (y/n)?: ")
            
            else:
                return "No operations available for this choice!"

    #Analyze numeric column
    def analyze_column(df):
        continue_choice = 'y'
        while continue_choice == 'y':
            print("\n")
            print("ANALYZE NUMERIC COLUMN".center(40, '='))

            # non_numeric_cols = [columns for columns in df.columns if columns not in numeric_columns]
            # non_numeric_cols_df = df.select_dtypes(exclude=['number'])
            
            print(f"Available Numeric Columns: {", ".join(numeric_columns)}\n")
            # print(f"Non-numeric columns: {", ".join(non_numeric_cols)}\n")

            column_name = input("Enter the column name you want to analyze: ").strip().title()
            
            if column_name not in numeric_columns:
                return f"Can't operate on non-numeric '{column_name}' column"

            print("\nChoose Operation:")
            print("1.Total (Sum)")
            print("2.Average (Mean)")
            print("3.Minimum Value")
            print("4.Maximum Value")
            print("5.Count of Values")
            
            try:
                column_choice = int(input("Enter you choice (1-5): "))
            except ValueError:
                print("Enter numerical choices!")

            def total(df_dict):
                return f"\nTotal (sum) of {column_name} = {df_dict['numeric_columns_sum'][column_name]:.2f}"
            
            def average(df_dict):
                return f"\nAverage (mean) of {column_name} = {df_dict['numeric_columns_average'][column_name]:.2f}"
            
            def min_value(df_dict):
                return f"\nMinimum value from {column_name} = {df_dict['numeric_columns_min'][column_name]:.2f}"
            
            def max_value(df_dict):
                return f"\nMaximum value from {column_name} = {df_dict['numeric_columns_max'][column_name]:.2f}"
            
            def count_values(df_dict):
                return f"\nCount of values from {column_name} = {df_dict['numeric_columns_count'][column_name]:.2f}"
            
            if column_choice == 1:
                print("\nTOTAL:", total(df_dict))
                continue_choice = input("Stay on this menu (y/n)?: ")

            
            elif column_choice == 2:
                print(average(df_dict))
                continue_choice = input("Stay on this menu (y/n)?: ")

            elif column_choice == 3:
                print(min_value(df_dict))
                continue_choice = input("Stay on this menu (y/n)?: ")

            elif column_choice == 4:
                print(max_value(df_dict))
                continue_choice = input("Stay on this menu (y/n)?: ")

            elif column_choice == 5:
                print(count_values(df_dict))
                continue_choice = input("Stay on this menu (y/n)?: ")
            
            else:
                print("No operations available for this choice!")

    #Check missing values
    def check_missing_values(df):
        print("\n")
        print("Missing values".center(40,'='))
        column_choice = input("Enter a column to find missing values: ").lstrip().rstrip()
        try:
            return f"Total Null values = {df[column_choice].isnull().sum()}\n"
        except KeyError:
            return "Column not found!"
    
    
    #Text histogram
    def text_histogram(df):
        print("\n")
        print("Text Histogram".center(40,"="))
        numeric_columns = ['Sales', 'Profit', 'Quantity', 'Discount']
        print(f"Available Numeric Columns: {", ".join(numeric_columns)}")
        column_name = input("Enter the column name you want the histogram of: ").title().strip()
        
        try:
            range_input_1 = float(input("Enter the starting value: "))
            range_input_2 = float(input("Enter the ending value: "))
            filtered_data = df.loc[
                                df[column_name].between(range_input_1, range_input_2), column_name]
            plt.figure(figsize=(8, 6))
            sns.histplot(data=filtered_data, bins=20)
            plt.title(f'Text histogram of {column_name} ({range_input_1} - {range_input_2})')
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.show()

        except ValueError:
            print("Enter numerical ranges!")

        except KeyError:
            print(f"Invalid column name '{column_name}'!")

        

    df_dict = load_csv()
    if df_dict:
        
        #Main Menu
        continue_choice = 'y'
        while continue_choice == 'y':
            print("\n")
            print("Welcome to the Command-Line Data Analytics Tool".center(70, '='))
            print("Main Menu:")
            print("1.Preview Data")
            print("2.Analyze Numeric Column")
            print("3.Check Missing Values")
            print("4.Text histogram")
            print("5.Exit")

            try:
                operation_choice = int(input("Enter your choice(1-5): "))
            except ValueError:
                print("Enter numerical choices!")

            if operation_choice == 1:
                preview_data(df_dict['df'])
                try:
                    continue_choice = input("Do you want to continue (y/n)?: ")
                except ValueError:
                    print("Enter numerical choices!")

            elif operation_choice == 2:
                analyze_column(df_dict['df'])
                try:
                    continue_choice = input("Do you want to continue (y/n)?: ")
                except ValueError:
                    print("Enter numerical choices!")

            elif operation_choice == 3:
                print(check_missing_values(df_dict['df']))
                try:
                    continue_choice = input("Do you want to continue (y/n)?: ")
                except ValueError:
                    print("Enter numerical choices!")

            elif operation_choice == 4:
                text_histogram(df_dict['df'])
                try:
                    continue_choice = input("Do you want to continue (y/n)?: ")
                except ValueError:
                    print("Enter numerical choices!")
                
            elif operation_choice == 5:
                print("\n")
                print("Thank you for using Data Analytics CLI!".center(70, "="))
                break

            else:
                print("No operation available for this choice!")
        else:
            print("\n")
            print("Thank you for using Data Analytics CLI!".center(70, "="))

if __name__ == '__main__':
    cli_analytics_tool()
        