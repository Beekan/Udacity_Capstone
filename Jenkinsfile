pipeline
{
    

    agent any
    stages
    {
        stage('initial slack message')
        {
            steps
            {
                sh 'echo hello world'
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
                        sh 'aws s3 ls'
                        
                        
                        
                    }
                }
            }
        }       
        
    }
}