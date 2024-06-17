from .bootstrap import bootstrap

def default_list(data):
    lignes = ""
    header = ''
    for head in data['heads']:
        header += f'<th class="bg-light" scope="col">{head}</th>'
    for item in data['dataList']:
        tr = "<tr>"
        for i in item:
            tr += f"<td>{i}</td>"
        tr += "</tr>"
        lignes += tr

    #set footer
    tr = '<tr>'
    i = 0
    for item in data['heads']:
        if i == 0:
            value = "Total"
        else:
            value = ''
            for thfoot in data['totalData']:
                print(thfoot)
                print(item)
                if thfoot['key'] == item:
                    value = thfoot['value']
            
        tr += f"<th>{value}</th>"
        i += 1
    tr += "</tr>"
    lignes += tr
    
    content = f"""
    <!DOCTYPE html>
        <html>
            <title>Exemple de PDF avec Bootstrap</title>
        <head>
            <style>
                {bootstrap}
                body {{
                    font-family: Arial, sans-serif;
                }}
                h1 {{
                    color: blue;
                }}
                th, td {{
                    padding-top: 5px !important;
                    padding-bottom: 5px !important;
                }}
                body{{
                    width: 100%;
                }}
                thead, th{{
                    background-color: gray !important;
                }}
            </style>
        </head>
    <body>
        <div class="">
            <header class="d-flex justify-content-start">
                
                <div class="">
                    <img width="100" 
                        src="{data['group']['groupeLogo'] if f"data:image/png;base64,{data['group'].get('groupeLogo')}" else ''}" class="border" alt="logo">
                </div>
                <div class="ml-2 mt-1">
                    <h4 class="text-uppercase mb-0"><strong>{data['group']['groupeName']}</strong></h4>
                    <p class="text-uppercase mb-0"><strong>{data['group']['groupDevise']}</strong></p>
                    <p class="text-uppercase mb-0"><strong>{data['group']['siteName']}</strong></p>
                    <small>
                        { '<span class="mr-2"></span>Tél: ' + data['group']['siteContact'] if data['group'].get('siteContact') else ''}
                        <span class="">
                            { ' / ' + data['group']['siteAddress'] if data['group'].get('siteAddress') else ''}
                        </span>
                    </small>
                </div>
            </header>
        <hr>
        <div class="text-center">
            <h4 class="text-center border p-2 bg-light">{data['title']}</h4>
        </div>
        <div class="">
            
                <table class="table w-100 table-bordered">
                <thead>
                    <tr class="bg-light">{header}</tr>
                </thead>
                <tbody>
                    {lignes}
                </tbody>
                </table>
            
            <hr>
            
            <div class="row">
                <div class="col-6 text-start"><strong>smaartpro@zandosoft-2024</strong></div>
            </div>
        </div>
      </body>
    </html>
    """
    return content
    