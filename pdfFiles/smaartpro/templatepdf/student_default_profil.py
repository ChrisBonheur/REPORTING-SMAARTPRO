from .bootstrap import bootstrap

def default_profile_student(fiche):
    default_profil_student = f"""
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
    <div class="">
        <header class="d-flex justify-content-start">
            
            <div class="">
                <img  width="100" src="{fiche['group']['groupeLogo'] if f"data:image/png;base64,{fiche['group'].get('groupeLogo')}" else ''}" class="border" alt="logo">
            </div>
            <div class="ml-2 mt-1">
                   <h4 class="text-uppercase mb-0"><strong>{fiche['group']['groupeName']}</strong></h4>
                    <p class="text-uppercase mb-0"><strong>{fiche['group']['groupDevise']}</strong></p>
                    <p class="text-uppercase mb-0"><strong>{fiche['group']['siteName']}</strong></p>
                    <small>
                        { '<span class="mr-2"></span>Tél: ' + fiche['group']['siteContact'] if fiche['group'].get('siteContact') else ''}
                        <span class="">
                            { ' / ' + fiche['group']['siteAddress'] if fiche['group'].get('siteAddress') else ''}
                        </span>
                    </small>
            </div>
        </header>
        <hr>
        <div class="text-center">
            <h2 class="text-center border p-2 bg-light">Fiche individuelle de l'élève</h2>
        </div>
        <div class="row ">
            <div class="col-4 border-right bg-light">
                <div class="d-flex justify-content-center bg-light">
                <img
                    style="max-width: 200px; min-height: 220px;"
                    src="{fiche['student']['photo'] if f"data:image/png;base64,{fiche['student'].get('photo')}" else ''}"
                    class="card-img-top border rounded"
                    alt="photo élève"
                />
                </div>

                <div class="d-flex justify-content-center mt-4">
                    <img
                    width="150px"
                    src="data:image/png;base64,{fiche['student']['qrCode'] if f"data:image/png;base64,{fiche['student'].get('qrCode')}" else ''}"
                    class="border rounded-0"
                    alt="Qr-code"
                    />
                </div>
            </div>

        <div class="col-8">
            <div class="row">
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Nom(s) </label></div>
                <div class="col-8">: <strong>{fiche['student']['firstName']}</strong></div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Prénom(s) </label></div>
                <div class="col-8">: <strong>{fiche['student']['lastName']}</strong></div>
            </div>
            
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Classe  </label></div>
                <div class="col-8">: <strong>{fiche['student']['siteClassTitle']}</strong></div>
            </div>
            
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Date de naissance  </label></div>
                <div class="col-8">: <strong>{fiche['student']['dateOfBirth']}</strong></div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Lieu de naissance </label></div>
                <div class="col-8">: <strong>{fiche['student']['birthCity']}</strong></div>
            </div>


            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Civilité </label></div>
                <div class="col-8">: {'Garçon' if fiche['student']['civility'] == 1 else 'Fille'}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Email </label></div>
                <div class="col-8">: {fiche['student']['email']}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Nationalité (Pays) </label></div>
                <div class="col-8">: {fiche['student']['nationalityTitle']}</div>
            </div>


            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Adresse </label></div>
                <div class="col-8">: {fiche['student']['address']}</div>
            </div>
    
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Contact </label></div>
                <div class="col-8">: {fiche['student']['phone1'] + " " + fiche['student']['phone2']}</div>
            </div>
    
            </div>
        </div>

        </div>

        <hr>
        
        <div class="row">
            <div class="col-6 text-start"><strong>smaartpro@zandosoft-2024</strong></div>
            <div class="col-6 text-end"> <a target="_blank" href="https://smaartpro.zandosoft.com/" title="ouvrir smaartpro">www.smaartpro.zandosoft.com</a> </div>
        </div>
    
    </div>
        </body>
        </html>
    """
    return default_profil_student
    