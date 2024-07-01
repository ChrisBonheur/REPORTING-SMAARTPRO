from .bootstrap import bootstrap

def recu_frais(data):
    lignes = ""
    for item in data['transactions']:
        tr = "<tr>"
        tr += f"<td>{item['label']}</td>"
        tr += f"<td>{item['amount']}</td>"
        tr += "</tr>"
        lignes += tr

    lines = [f"""<tr><td>{trans['label']}</td><td >{trans['amount']}</td></tr>""" for trans in data['transactions']]
    
    content = f"""
    <!DOCTYPE html>
        <html>
            <title>Caisse</title>
        <head>
            <style>
                {bootstrap}
                body{{
                    width: 595px;
                }}
                .text-danger strong {{
                        color: #9f181c;
                    }}
                    .receipt-main {{
                        background: #ffffff none repeat scroll 0 0;
                        border-bottom: 2px solid #333333;
                        border-top: 2px solid #9f181c;
                        margin-top: 50px;
                        margin-bottom: 50px;
                        padding: 40px 30px ;
                        box-shadow: 0 1px 21px #acacac;
                        color: #333333;
                        font-family: open sans;
                    }}
                    .receipt-main p {{
                        color: #333333;
                        font-family: open sans;
                        line-height: 1.42857;
                    }}
                    .receipt-footer h1 {{
                        font-size: 15px;
                        font-weight: 400 ;
                        margin: 0 ;
                    }}

                    .receipt-main thead {{
                        background: #414143 none repeat scroll 0 0;
                    }}
                    .receipt-main thead th {{
                        color:#fff;
                        background: gray;
                    }}
                    .receipt-right h5 {{
                        font-size: 16px;
                        font-weight: bold;
                        margin: 0 0 7px 0;
                    }}
                    .receipt-right p {{
                        font-size: 12px;
                        margin: 0px;
                    }}
                    .receipt-right p i {{
                        text-align: center;
                        width: 18px;
                    }}
                    .receipt-main td {{
                        padding: 9px 20px ;
                    }}
                    .receipt-main th {{
                        padding: 5px 20px ;
                    }}
                    .receipt-main td {{
                        font-size: 13px;
                        font-weight: initial ;
                    }}
                    .receipt-main td p:last-child {{
                        margin: 0;
                        padding: 0;
                    }}	
                    .receipt-main td h2 {{
                        font-size: 20px;
                        font-weight: 900;
                        margin: 0;
                        text-transform: uppercase;
                    }}
                    .receipt-header-mid .receipt-left h1 {{
                        font-weight: 100;
                        text-align: right;
                        text-transform: uppercase;
                    }}
                    .receipt-header-mid {{
                        margin: 10px 0;
                        overflow: hidden;
                    }}
                    
                    #container {{
                        background-color: #dcdcdc;
                    }}
            </style>
        </head>
<body>

<div class="container col">
    <div class="receipt-main m-auto mt-0 ">
            <div class="row mb-0">
                <div class="receipt-header row mt-0">
                    <div class="col-12 d-flex">
                        <div class="receipt-left ">
                            <img class="img-responsive mr-4" alt="iamgurdeeposahan" src="{data['groupeLogo'] if data.get('groupeLogo') else '' }" style="width: 71px; border-radius: 43px; margin-left: 1em;">
                        </div>
                        <div class="">
                            <div class="receipt-right">
                                <h4 class="text-end mb-0">{data['groupeName']}</h4>
                                <p>{data['groupeDevise']} <i class="fa fa-envelope-o"></i></p>
                                <p>{data['siteContact']} <i class="fa fa-phone"></i></p>
                                
                                <h5>{data['siteName']} <i class="fa fa-location-arrow"></i></h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <hr class="my-0 mt-1">
            <div class="row">
                <div class="receipt-header receipt-header-mid row pl-1 w-100">
                    <div class="col-7 text-left">
                        <div class="receipt-right">
                            <p>Nom(s) : <b>{data['eleveName']}</b></p>
                            <p>Prénom(s) : <b>{data['elevePrenom']} </b></p>
                            <p>Matricule : <b>{data['matricule']} </b></p>
                            <p>Classe : <b>{data['niveau']} </b></p>
                            <p>Annee : <b>{data['scholarYear']} </b></p>
                        </div>
                    </div>
                    <div class="col-5">
                        <div class="w-100">
                            <h5 class="text-uppercase text-end w-100">Reçu #{data['recuNumber']}</h5>
                            <div class="receipt-right">
                                <p>Agent : <b>{data['printerAgent']}</b></p>
                                <p>Caisse : <b>{data['caisse']}</b></p>
                                <p>Date : <b>{data['dateRecu']}</b></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
        
            <table class="table table-bordered">
                <tr style="background-color: gray !important; color: white">
                    <th style="background-color: gray !important; color: white">Description</th>
                    <th style="background-color: gray !important; color: white" >Montant</th>
                </tr>
                {lignes}
                
                <tr>
                    <td style="width: 70% !important" class="text-right"><h2>Total:</h2></td>
                    <td class="text-left text-danger">
                        <strong> {data['totalAmountTransaction']}</strong>
                    </td>
                </tr>
            </table>
            
            <div class="row">
                <div class="receipt-header receipt-header-mid receipt-footer row w-100">
                    <div class="col-6">
                        <div class="col-12 text-left">
                            <div class="receipt-right">
                                <h5 style="color: rgb(140, 140, 140);">smaartschool</h5>
                            </div>
                        </div>
                        <div class="col-12">

                        </div>
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
            </div>
            
    </div>    
</div>

</body>
        </html>
    """
    return content
    