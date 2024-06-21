from .bootstrap import bootstrap
from smaartpro.utils import week_days, get_current_datetime

def closed_Cash(data):
    lignes = ""
    
    for item in data['transactions']: 
        lignes += f"""<tr>
            <td scope="" class="dateOperation" style="width: 170px;">
                <div class="row my-0 py-0">
                    <div class="col-4 my-0 py-0"><span class="text-muted">O. </span></div>
                    <div class="col my-0 py-0">: {item['transactionDate']}</div>
                </div>
                <div class="row my-0 py-0">
                    <div class="col-4 py-0 my-0 py-0"><span class="text-muted">V. </span></div>
                    <div class="col py-0 my-0 py-0">: {item['valueDate']}</div>
                </div>
            </td>
            <td>{item['description']}</td>
            <td>{item['compte']}</td>
            <td>{item['debitAmount']}</td>
            <td>{item['creditAmount']}</td>
        </tr>"""
    
    content = f"""
<!DOCTYPE html>
<html>
    <title>Exemple de PDF avec Bootstrap</title>
<link rel="stylesheet"  href="./boot.css">
<head>
    <style>
       {bootstrap}
        body {{
            font-family: Arial, sans-serif;
        }}
        th, td {{
            padding-top: 5px !important;
            padding-bottom: 5px !important;
        }}

        iframe{{
            width: 100%;
            height: 760px;
        }}

        .dateOperation{{
            font-size: 0.7em;
        }}

    </style>
</head>
<body>
    <div class="container border">
        <div class="">
            <header class="card rounded-0 p-2">
                <div class="row">
                    <div class="col-md-6 d-flex justify-content-start">
                        <header class="d-flex justify-content-start">
                            
                            <div class="">
                                <img width="100" 
                                    src="{data['group']['groupeLogo'] if f"data:image/png;base64,{data['group'].get('groupeLogo')}" else ''}" class="border" alt="logo">
                            </div>
                            <div class="ml-2 mt-1">
                                <h4 class="text-uppercase mb-0"><strong>{data['group']['groupeName']}</strong></h4>
                                <p class="text-uppercase mb-0"><strong>{data['group']['groupDevise']}</strong></p>
                                <small>
                                    { '<span class="mr-2"></span>Tél: ' + data['group']['siteContact'] if data['group'].get('siteContact') else ''}
                                    <span class="">
                                        { ' / ' + data['group']['siteAddress'] if data['group'].get('siteAddress') else ''}
                                    </span>
                                </small>
                            </div>
                        </header>
                    </div>
                    <div class="col-md-6">
                        <h2 class="d-flex text-secondary justify-content-end w-100 text-uppercase">RELEVE de caisse</h2>
                    </div>
                </div>
            </header>
            

            <div class="row">
                <div class=" col-7 pr-0 my-2">
                    <div class="card border border-right-0 bg-light rounded-0 p-2">
                        <div>
                            <span class="text-secondary">Site :</span>
                            <span class="text-dark">{data['group']['siteName']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">Année scolaire : </span>
                            <span class="text-dark">{data['group']['schoolYear']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">N de compte :</span>
                            <span class="text-dark">{ data['sold']['compte_caisse'] }</span>
                        </div>
                    </div>
                </div>
                <div class=" col-5 pl-0 my-2">
                    <div class="card h-100 border pt-2 border-left-0 bg-light">
                        <div><span class="text-secondary">Date </span><span class="text-decoration-underline">{ data['sold']['closureDateTime'] }</span></div>
                        <h3>CAISSE: {data['sold']['caisse_name']}</h3>
                    </div>
                </div>
            </div>
            <div class="my-2">
                <span class="text-secondary">Solde d'ouverture :</span> <strong class="border p-1"> {data['sold']['openingBalance']} </strong>
            </div>
            <table class="table w-100 table-bordered">
                <thead>
                  <tr class="bg-light p-0">
                    <th scope="col">Date </th>
                    <th scope="col">Libellé de l'opération</th>
                    <th scope="col">Compte</th>
                    <th scope="col">DEBIT</th>
                    <th scope="col">CREDIT</th>
                  </tr>
                </thead>
                <tbody>
                    {lignes}
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3">Total</td>
                        <td class="bg-light"><strong>{data['sold']['totalCashOut']}</strong></td>
                        <td class="bg-light"><strong>{data['sold']['totalCashIn']}</strong></td>
                    </tr>
                </tfoot>
            </table>
            <div class="row">
                <div class="col-6" style="font-size: 0.8em;">
                    <div><span class="text-secondary">Imprimé par </span> {data['printerName']}</div>
                    <div style="margin-left: 60px;"><span class="text-secondary">le</span> -</div>
                </div>
                <div class="col-6 d-flex justify-content-end">
                    <div><span class="text-secondary">Solde de fermeture</span> <strong class="border p-1">{data['sold']['closingBalance']}</strong></div>
                </div>
            </div>
            <hr class="mb-0">
            
            <div class="row mt-0">
                <div class="col-6 text-start"><strong>smaartschool@zandosoft-2024</strong></div>
            </div>
            
            </div>
    </div>


   
</body>
</html>

    """
    return content