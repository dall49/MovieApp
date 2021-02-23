
node {
	checkout scm
	def PIPENV = "~/.local/bin/pipenv"
	def REGISTRY = "redalegzali"

	stage("Build") {
		dir("restful-api") {
			sh "pip3 install pipenv"
			sh "${PIPENV} install"
		}
	}

	stage("Test") {
		def PORT = 3306
		def ROOT = "secret_root"
		def DB	 = "movieapp"
		def USER = "movieapp"
		def PASS = "secret_user"
		try {
			docker.image("mariadb:latest").withRun("-p ${PORT}:${PORT} -e MYSQL_ROOT_PASSWORD=${ROOT} -e MYSQL_DATABASE=${DB} -e MYSQL_USER=${USER} -e MYSQL_PASSWORD=${PASS}") { c ->
				sh "while ! mysqladmin ping -h0.0.0.0 --silent; do sleep 1; done"
				dir("restful-api") {
					withEnv(["DATABASE=${DB}","DBUSER=${USER}","PASSWORD=${PASS}"]){
						sh "${PIPENV} run python tests/MoviesTest.py"
						sh "${PIPENV} run python tests/CategoriesTest.py"
					}
				}
			}
		}
		catch (Exception e) {
			error "Unable to launch tests.Probably because something is running on port 3306."
		}
	}

	stage("Deploy") {
		docker.withRegistry("" , "DockerCreds") {
			dir("restful-api") {
				def restapi = docker.build("${REGISTRY}/restapi")
				restapi.push("latest")
			}
			dir("web-app") {
				def webapp = docker.build("${REGISTRY}/webapp")
				webapp.push("latest")
			}
		}
	}

	stage("Run") {
		sh "docker-compose build"
		try {
			sh "docker-compose up -d"
		}
		catch (Exception e) {
			error "Unable to start services.Probably because something is running on port 80 or 8000."
		}
		finally {
			sh "docker system prune -f"
		}
	}

}
