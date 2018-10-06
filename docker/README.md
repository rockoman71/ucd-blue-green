# ucd-blue-green

ref: https://developer.ibm.com/urbancode/docs/kubernetes-blue-green-deployments-working-example/#hello

docker build -t bgdemo .

docker login mycluster.icp:8500

docker tag bgdemo:latest mycluster.icp:8500/devops/bgdemo:v1

docker push mycluster.icp:8500/devops/bgdemo
