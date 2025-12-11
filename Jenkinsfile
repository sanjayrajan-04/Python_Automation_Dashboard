\
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'pytest tests/ --html=reports/report.html --self-contained-html'
      }
    }
    stage('Publish Report') {
      steps {
        // publishHTML requires the plugin; this snippet shows the intent
        publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'reports', reportFiles: 'report.html', reportName: 'PyTest HTML Report'])
      }
    }
  }
}
