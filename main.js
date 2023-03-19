const giturl = "http://api.github.com/users/";
function buscar(){
    var usuario = document.querySelector("#username").value
    fetch(giturl+usuario)
        .then(res => res.json())
        .then(data => {console.log(data)
                        if ("message" in data){
                            document.querySelector("#estado").innerHTML = "NO SE HA ENCONTRADO EL USUARIO"
                            document.querySelector("#estado").className = "nofound"
                        }
                        else{
                        document.querySelector("#estado").className = "found"
                        document.querySelector("#user_avatar").src = data["avatar_url"]
                        document.querySelector("#user_login").innerHTML = "user: "+data["login"]
                        document.querySelector("#user_id").innerHTML = "id: "+data["id"]
                        document.querySelector("#user_name").innerHTML = ""+data["name"]
                        document.querySelector("#user_location").innerHTML = "location: "+data["location"]
                        document.querySelector("#user_twitter").innerHTML = "@"+data["twitter_username"]
                        document.querySelector("#user_blog").innerHTML = "blog: "+data["blog"]
                        document.querySelector("#user_created").innerHTML = ("creado en: "+data["created_at"]).slice(0,21)
                        document.querySelector("#user_repos").innerHTML = "repositorios: "+data["public_repos"]
                        document.querySelector("#user_frs").innerHTML = "followers: "+data["following"]
                        document.querySelector("#user_fng").innerHTML = "followings: "+data["followers"]}
})
}