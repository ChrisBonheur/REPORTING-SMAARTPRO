from .bootstrap import bootstrap
from smaartpro.utils import week_days

def generateTimeLine(day):
    return f"""
        <td>
            {day['matiere']}
            <br>
            <div class="info-sup text-danger text-truncate my-1">
              {'P: ' + day['teacher'] if day.get('teacher') else ''}
            </div>
    
            <div class="info-sup text-primary text-truncate my-0">
                {'S: ' + day['salle'] if day.get('salle') else ''}
            </div>
        </td>
    """

def timeslot(data):  
    content = ""
    for line in data['data']:
        #buil  line tr
        tr = f"""<tr> <th scope="row">{line['hour']}</th>"""
        tds = ""
        #add all td for tr
        for day in week_days:
            tds += generateTimeLine(line[day])
        tr += tds
        tr += "</tr>" #close tr
        content += tr
    
    data_slot = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        {bootstrap}
        body {{
            font-family: Arial, sans-serif;
        }}

        iframe{{
            width: 100%;
            height: 760px;
        }}


        tr td{{
            padding: 0.5em 0.5em;
            height: 7em !important;
        }}
        tr th{{
           padding: 2em;
           background: rgb(182, 179, 179);
           width: 150px;
        }}
        
        .text-center{{
            text-align: center
        }}


    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 d-flex justify-content-start">
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
            </div>

            <div class="col-12 d-flex justify-content-start align-items-bottom">
                <h4 class="text-center w-100 col-12">{data['title']}</h4>
            </div>
        </div>

        <table class="table table-bordered">
            <thead>
              <tr class="">
                <th class="bg-light border-light" scope="col"></th>
                <th scope="col">Lundi</th>
                <th scope="col">Mardi</th>
                <th scope="col">Mercredi</th>
                <th scope="col">Jeudi</th>
                <th scope="col">Vendredi</th>
                <th scope="col">Samedi</th>
                <th scope="col">Dimanche</th>
              </tr>
            </thead>
            <tbody>
                {content}
            </tbody>
          </table>
    </div>
</body>
</html>

    """
    return data_slot