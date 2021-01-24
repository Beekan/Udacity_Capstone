pipeline
{
    environment 
    {
        imageName = 'beekoan/udacity_capstone'
        registryCredential = 'dockerhub'
    }
    

    agent any
    stages
    {   
        
        stage('linting Docker')
        {
            steps
            {
                sh 'hadolint Dockerfile'
            }
        }

        stage('Build Docker')
        {
            steps
            {
                script
                {
                    sh 'docker build --tag=api .'
                }
            }
        }

        stage('Push Docker')
        {
            steps
            {
                script
                {
                    withDockerRegistry([url:"", credentialsId: "dockerhub"])
                    {
                        sh 'docker tag api beekoan/udacity_capstone'
                        sh 'docker push beekoan/udacity_capstone'
                    }
                }
            }
        }

        stage('Deployment')
        {
            steps
            {
                script
                {
                    withAWS(credentials: 'AWScred', region: 'us-west-2')
                    {
                        sh 'aws eks update-kubeconfig --name capstonebeeko'
                        sh 'kubectl config use-context $(aws eks describe-cluster --name capstonebeeko | jq -r ."cluster"."arn")'
                        sh 'kubectl apply -f cluster.yml'
                        sh 'kubectl get nodes'                        
                    }
                }
            }
        }       
        
    }
}