
def get_profile(groupeName, groupeLogo, groupeSlogan, siteAdress, siteContact, nom, prenom, photo, qr, civility, email, roles, nationality, country, city, area, adress, contact):
    default_profil_agent = f"""
    <div class="">
        <header class="d-flex justify-content-start">
            
            <div class="">
                <img width="100" src="data:image/png;base64,{groupeLogo}" class="border" alt="logo">
            </div>
            <div class="ml-2 mt-1">
                <h4 class="text-uppercase mb-0"><strong>{groupeName}</strong></h4>
                <h5 class="mt-0 mb-0">{groupeSlogan}</h5>
                <p class="mt-0 mb-0">{siteAdress}</p>
                <p class="mt-0">{siteContact}</p>
            </div>
        </header>
        <hr>
        <div class="text-center">
            <h2 class="text-center border p-2 bg-light">Fiche individuelle de l'agent</h2>
        </div>
        <div class="row ">
            <div class="col-4 border-right bg-light">
                <div class="d-flex justify-content-center bg-light">
                <img
                    style="max-width: 200px; min-height: 220px;"
                    src="data:image/jpg;base64,{photo}"
                    class="card-img-top border rounded"
                    alt="photo agent"
                />
                </div>

                <div class="d-flex justify-content-center mt-4">
                    <img
                    width="100"
                    src="data:image/png;base64,{qr}"
                    class="border rounded-0"
                    alt="Qr-code"
                    />
                </div>
            </div>

        <div class="col-8">
            <div class="row">
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Nom(s) </label></div>
                <div class="col-8">: <strong>{nom}</strong></div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Prénom(s) </label></div>
                <div class="col-8">: <strong>{prenom}</strong></div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Civilité </label></div>
                <div class="col-8">: { civility }</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Email </label></div>
                <div class="col-8">: {email}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Rôles </label></div>
                <div class="col-8">: {roles}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Nationalité (Pays) </label></div>
                <div class="col-8">: {nationality}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Pays de résidence </label></div>
                <div class="col-8">: { country }</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Ville de résidence :</label></div>
                <div class="col-8">: { city }</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Arrondissement </label></div>
                <div class="col-8">: {area}</div>
            </div>

            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Adresse </label></div>
                <div class="col-8">: {adress}</div>
            </div>
    
            <div class="form-group mb-4 col-12 row">
                <div class="col-4"><label for="" class="mb-0 text-secondary">Contact </label></div>
                <div class="col-8">: {contact}</div>
            </div>
    
            </div>
        </div>

        </div>

        <hr>
        
        <div class="row">
            <div class="col-6 text-start"><strong>smaartpro@zandosoft-2024</strong></div>
            <div class="col-6 text-end"> <a target="_blank" href="https://managersmaartpro.zandosoft.com/" title="ouvrir managersmaartpro">www.managersmaartpro.zandosoft.com</a> </div>
        </div>
    
    </div>
    """
    return default_profil_agent
    