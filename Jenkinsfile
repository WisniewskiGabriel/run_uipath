pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        echo INICIANDO
      }
    }
    stage('hello') {
      steps {
        python.exe main.py
      }
    }
  }
}