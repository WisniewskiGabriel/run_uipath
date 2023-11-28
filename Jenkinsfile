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
        sh 'python main.py'
      }
    }
  }
}