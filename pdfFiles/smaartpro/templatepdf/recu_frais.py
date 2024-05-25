from .bootstrap import bootstrap

def recu_frais(data):
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
            <title>Caisse</title>
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
                    <div class="col-8 d-flex justify-content-start">
                        <div class="">
                            <img width="100" src="{data['groupeLogo'] if data.get('groupeLogo') else '' }" class="border" alt="logo">
                        </div>
                        <div class="ml-2 mt-1">
                            <h4 class="text-uppercase mb-0"><strong>{data['groupeName']}</strong></h4>
                            <h5 class="mt-0 mb-0">{data['groupeDevise']}</h5>
                            <p class="mt-0 mb-0"></p>
                        </div>
                    </div>
                    <div class="col-4">
                        <h2 class="d-flex text-secondary justify-content-end align-items-center w-100 text-uppercase">reçu de caisse</h2>
                    </div>
                </div>
                <hr>
                <div class="row">
                    <div class="col-12">
                        <table>
                            <tr>
                                <td class="text-muted">Nom</td>
                                <td>: {data['eleveName']}</td>
                                <td class="text-muted pl-4">Prenoms</td>
                                <td>: {data['elevePrenom']}</td>
                            </tr>
                            <tr>
                                <td class="text-muted">Matricule</td>
                                <td>: </td>
                                <td class="text-muted pl-4">Niveau</td>
                                <td>: {data['niveau']}</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </header>
            
<div class="row mt-2">
                <div class="col-7 pr-0">
                    <div class="card border-top-0 border-right-0 rounded-0 p-2 bg-light">
                        <table>
                            <tr>
                                <td><span class="text-secondary">Site </span></td>
                                <td>: <span class="text-dark">{data['siteName']}</span></td>
                            </tr>
                            <tr>
                                <td><span class="text-secondary">Adresse </span></td>
                                <td>: <span class="text-dark">{data['siteAdress']}</span></td>
                            </tr>
                            <tr>
                                <td><span class="text-secondary">Tél </span></td>
                                <td>: <span class="text-dark">{data['siteContact']}</span></td>
                            </tr>
                        </table>
                    </div>
                </div>
                <div class="col-5  d-flex flex-column align-items-end justify-content-center pl-0">
                    <div class="w-100 h-100 w-100 border border-left-0 bg-light">
                        <div>
                            <span class="text-secondary">Caisse :</span>
                            <span class="text-dark">{data['caisse']} </span>
                        </div>
                        <div>
                            <span class="text-secondary">Année scolaire :</span>
                            <span class="text-dark">{data['scholarYear']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">Date :</span>
                            <span class="text-dark">{data['dateRecu']}</span>
                        </div>
                        <div>
                            <span class="text-secondary">N Reçu :</span>
                            <span class="text-dark">{data['recuNumber']}</span>
                        </div>
                    </div>
                </div>
            </div>
            <table class="table w-100 table-bordered mt-2">
                <thead>
                    <tr class="bg-light p-0">
                        <th scope="col">Libellé de l'opération</th>
                        <th scope="col">Type</th>
                        <th scope="col">Catégorie</th>
                        <th scope="col">Paiement</th>
                        <th scope="col">Montant</th>
                    </tr>
                </thead>
                    {lignes}
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="4">Total</td>
                        
                        <td class="bg-light"><strong>{data['totalAmountTransaction']}</strong></td>
                    </tr>
                </tfoot>
            </table>
            <div class="row">
                <div class="col-6" style="font-size: 0.8em;">
                    <div><span class="text-secondary">Imprimé par </span> Bonheur Mafoundou</div>
                    <div style="margin-left: 60px;"> <span class="text-secondary">le</span> 16/08/2024</div>
                </div>
                <div class="col-6 d-flex justify-content-end">
                    <table class="table table-bordered">
                        <tr>
                            <th>Bénéficiaire</th>
                            <th>Caissier</th>
                        </tr>
                        <tr style="height: 100px;">
                            <td></td>
                            <td></td>
                        </tr>
                    </table>
                </div>
            </div>
            <hr class="mb-0">
            
                <div class="row mt-0">
                    <div class="col-6 text-muted"><span>smaartpro@zandosoft-2024</span></div>
                    <div class="col-6 text-end"><a href="http://www.smaartpro.zandosoft.com"></a></div>
                </div>
            
            </div>
    </div>

   
</body>
        </html>
    """
    return content
    