pipeline {
	agent any
	environment {
		PIPENV = "~/.local/bin/pipenv"
		ROOT = "secret_root"
		USER = "movieapp"
		PASS = "secret_user"
		DB = "movieapp"
		PORT = "3307"
	}
	stages {
		stage("Build") {
			steps {
				dir("restful-api") {
					sh "pip install pipenv"
					sh "${PIPENV} install"
				}
			}
		}
		stage("Test") {
			steps {
				sh "docker run -d --name db_test -p ${PORT}:${PORT} -e MYSQL_ROOT_PASSWORD=${ROOT} -e MYSQL_DATABASE=${DB} -e MYSQL_USER=${USER} -e MYSQL_PASSWORD=${PASS} mariadb:latest"
				sh "docker exec db_test bash -c 'while ! mysqladmin ping -h localhost -p${ROOT} --silent; do sleep 1; done'"
				dir("restful-api") {
					sh "${PIPENV} run python tests/MoviesTest.py"
					sh "${PIPENV} run python tests/CategoriesTest.py"
				}
			}
		}
		stage("Deploy") {
			steps {
				sh "docker system prune -f"
				sh "docker build -t redalegzali/restapi restful-api/"
				sh "docker build -t redalegzali/webapp web-app/"
				withCredentials([usernamePassword(credentialsId: "DockerCreds", passwordVariable: "pass", usernameVariable: "user")]) {
					sh "docker login -u ${user} -p ${pass}"
					sh "docker push redalegzali/restapi"
					sh "docker push redalegzali/webapp"
				}
			}
		}
		stage("Run") {
			steps {
				sh "docker-compose up --build"
			}
		}
	}
	post {
		always {
			sh "docker rm -f db_test"
			dir("restapi-api") {
				sh "${PIPENV} --rm"
			}
		}		
	}
}
