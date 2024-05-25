from .bootstrap import bootstrap

def journal_caisse(data):
    lignes = ""
    for item in data['transactions']:
        tr = "<tr>"
        for v in item.values():
            tr += f"<td>{v}</td>"
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
                body{{
                    width: 595px;
                }}
            </style>
        </head>
<body>

    <div class="container border">
        <div class="">
            <header class="card rounded-0 p-2">
                <div class="row">
                    <div class="col-md-6 d-flex justify-content-start">
                        <div class="">
                            <img width="100" src="data:image/png;base64,{data['groupeLogo']}" class="border" alt="logo">
                        </div>
                        <div class="ml-2 mt-1">
                            <h4 class="text-uppercase mb-0"><strong>{data['groupeName']}</strong></h4>
                            <h5 class="mt-0 mb-0">{data['groupeDevise']}</h5>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <h2 class="d-flex text-secondary justify-content-end w-100 text-uppercase">{data['title']}</h2>
                    </div>
                </div>
            </header>
            

            <div class="row">
                <div class=" col-7 pr-0 my-2">
                    <div class="card border border-right-0 bg-light rounded-0 p-2">
                        <div>
                            <span class="text-secondary">Site :</span>
                            <span class="text-dark">{data['siteName']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">Année scolaire :</span>
                            <span class="text-dark">{data['scholarYear']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">N de compte :</span>
                            <span class="text-dark">{data['compte']}</span>
                        </div>
                    </div>
                </div>
                <div class=" col-5 pl-0 my-2">
                    <div class="card h-100 border pt-2 border-left-0 bg-light">
                        <div><span class="text-secondary">Période du </span><span class="text-decoration-underline">{data['periode']}</span></div>
                        <h3>CAISSE {data['caisse']}</h3>
                    </div>
                </div>
            </div>
            <div class="my-2">
                <span class="text-secondary">Solde d'ouverture :</span> <strong class="border p-1">{data['openSold']}</strong>
            </div>
            <table class="table w-100 table-bordered">
                <thead>
                    <tr class="bg-light p-0">
                        <th scope="col">Date operation</th>
                        <th scope="col">Date valeur</th>
                        <th scope="col">Libellé de l'opération</th>
                        <th scope="col">Type</th>
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
                        <td colspan="5">Total</td>
                        
                        <td class="bg-light"><strong>{data['totalDebit']}</strong></td>
                        <td class="bg-light"><strong>{data['totalCredit']}</strong></td>
                    </tr>
                </tfoot>
            </table>
            <div class="row">
                <div class="col-6" style="font-size: 0.8em;">
                    <div><span class="text-secondary">Imprimé par </span> Bonheur Mafoundou</div>
                    <div style="margin-left: 60px;"> <span class="text-secondary">le</span> 16/08/2024</div>
                </div>
                <div class="col-6 d-flex justify-content-end">
                    <div><span class="text-secondary">Solde de fermeture</span> <strong class="border p-1">{data['closeSold']}</strong></div>
                </div>
            </div>
            <hr class="mb-0">
            
            <div class="row mt-0">
                <div class="col-6 text-start"><strong>smaartpro@zandosoft-2024</strong></div>
            </div>
            
            </div>
    </div>

   
</body>
        </html>
    """
    return content
    