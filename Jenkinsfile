pipeline{
    agent any
    environment{
       ArtifactId = "FlaskApp"
       Version = "1"
       Name = "FlaskApp"
       GroupId = "PythonFlask"
    }
    stages{
        // stage 1. Build
        stage ('Build'){
            steps {
                echo 'Build zip'
                sh 'zip -r main.zip main.py'
            }
        }

        // Stage2 : Testing
        stage ('Test'){
            steps {
                echo 'testing......'
            }
        }

        stage ('Send to Nexus'){
            steps {
               nexusArtifactUploader artifacts: [[artifactId: 'main', classifier: '', file: 'main.zip', type: 'zip']], credentialsId: 'a36a2635-878d-4704-87fc-f0a5541c482a', groupId: 'FlaskApp', nexusUrl: '192.168.0.6:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'PythonDeploy', version: '2'
            }
        }

        stage ('Deploy to docker'){
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: 'Ansible_ControlNode', 
                transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'ansible-playbook /home/ansibleadmin/deploydocker.yaml -i /etc/ansible/hosts',
                execTimeout: 120000, flatten: false, 
                makeEmptyDirs: false, noDefaultExcludes: false, 
                patternSeparator: '[, ]+', remoteDirectory: '', 
                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], 
                usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }
        }
    }
}