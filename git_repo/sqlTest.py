reqdCols = """
    SELECT SourceNonPHIcolumn
"""



query1 = f"""
    SELECT *
    FROM INFORMATION_SCHEMA.COLUMNS info INNER JOIN helper.IngestionDriver driv
    ON infor.TABLE_NAME = driv.TargetTable
"""