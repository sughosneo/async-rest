### Asynchronous REST API(s)

Building rest API is possibly one of the common activity which might have seen in any recent modern 
applications. It might not be that difficult to write a restful api than scaling it. Horizontal scaling with growing number of incoming
request is always be the challenge. Though there are many modern mechanism are available to perform horizontal scaling of any restful API(s). 
If you ask any engineer now days. Suggestion would come as follows.  
   
   1) Need to follow Microservices architectural pattern, so that individual services can be deployed multiple times to handle load.
   2) Rest API should be hosted with a server which is scalable itself and can handle millions of request.
   3) Use Kubernetes based deployment of service pods with multiple replication factor.
   4) Use of serverless framework (like - AWS lamnda, Azure Function) if cloud deployment is a choice.    
   5) Use the language (like - node.js) which are async in nature or using possibly Go.
   
there could be few more as well... But someone has to realize it's not only the deployment strategy or load balancing would actually 
help to scale one rest api. Rest API code itself needs to be capable of handling multiple request at once. 
If the Rest API itself is written as synchronous manner then it would be bit difficult for handling such request at scale. And particularly 
if the choice of programming language is Python then it has more challenges than normal.
Let's see how we can we write such rest API(s)

***```Synchronous Rest API :```*** 
-----------------------------------
- InfoSvcSync - API is actually has been written to handle incoming request synchronously.
- It has been written using **Falcon** library.
- Similarly it can be written using **Flask** library.
- Sample request and response looks to be something like as per below :

***Server :***
```python
     
    [2019-11-11 19:46:59.836968] Info api has been started and listening on http://0.0.0.0:8000/info
    [2019-11-11 19:47:10.376536] Received request ::[71e28113-564b-4f1c-a834-f0f4a8b10ee4]
    [2019-11-11 19:47:15.377474] Sending Response ::[{"result": "success", "id": "71e28113-564b-4f1c-a834-f0f4a8b10ee4"}]
    [2019-11-11 19:47:15.380326] Received request ::[8a52810f-861b-4a0d-b807-d9bcbdd51ae5]
    127.0.0.1 - - [11/Nov/2019 19:47:15] "GET /info HTTP/1.1" 200 67
    127.0.0.1 - - [11/Nov/2019 19:47:20] "GET /info HTTP/1.1" 200 67
    [2019-11-11 19:47:20.380666] Sending Response ::[{"result": "success", "id": "8a52810f-861b-4a0d-b807-d9bcbdd51ae5"}]
    [2019-11-11 19:47:20.381288] Received request ::[1f439d7e-d77c-4a5b-880b-6bbe07cd524e]
    [2019-11-11 19:47:25.381776] Sending Response ::[{"result": "success", "id": "1f439d7e-d77c-4a5b-880b-6bbe07cd524e"}]
    127.0.0.1 - - [11/Nov/2019 19:47:25] "GET /info HTTP/1.1" 200 67
    [2019-11-11 19:47:25.385762] Received request ::[0f2fea4e-3541-4ca4-b505-6b40dde579c7]
    127.0.0.1 - - [11/Nov/2019 19:47:30] "GET /info HTTP/1.1" 200 67
    [2019-11-11 19:47:30.386963] Sending Response ::[{"result": "success", "id": "0f2fea4e-3541-4ca4-b505-6b40dde579c7"}]
    [2019-11-11 19:47:30.389764] Received request ::[b4ceef33-9b35-463b-8160-42ffc7b27e16]
    127.0.0.1 - - [11/Nov/2019 19:47:35] "GET /info HTTP/1.1" 200 67
    [2019-11-11 19:47:35.391977] Sending Response ::[{"result": "success", "id": "b4ceef33-9b35-463b-8160-42ffc7b27e16"}]
    [2019-11-11 19:47:35.394669] Received request ::[024f1dd7-0868-4d2e-811f-7a2aba1c9098]
    [2019-11-11 19:47:40.394749] Sending Response ::[{"result": "success", "id": "024f1dd7-0868-4d2e-811f-7a2aba1c9098"}]
    127.0.0.1 - - [11/Nov/2019 19:47:40] "GET /info HTTP/1.1" 200 67
    
``` 

- If you notice each request is taking quite a bit of time to respond. That can be tracked based on the correlation id.
- Because of the response delay client also actually timed out while waiting on other task to get finish.

***```Asynchronous Rest API With aihttp library:```*** 
-----------------------------------    

- It's one of the other way of writing rest api which would perform async request and response.
- With help of aiohttp library we should be able to handle many more request than sync call. 
- If you notice request and response, you would notice pretty instantaneous.

***Server***

```python
        
[2019-11-11 19:53:46.248635] Received request ::[6cda0c89-7c34-4848-be05-8d30170bf247]
[2019-11-11 19:53:46.265541] Received request ::[fbfbb2f7-4610-4d11-92f2-f4a828d4afee]
[2019-11-11 19:53:46.266536] Received request ::[f6c07cb0-1246-47ac-b8c4-991753f74455]
[2019-11-11 19:53:46.266536] Received request ::[409a3598-90d3-45ac-8651-aa5c301741f5]
[2019-11-11 19:53:46.284487] Received request ::[b025a616-c9a0-4211-9097-788373ac9b9e]
[2019-11-11 19:53:46.284487] Received request ::[9467a0ad-4dae-4e3b-b5a1-e2ace255d1df]
[2019-11-11 19:53:46.285521] Received request ::[5520c1ba-bd6d-4671-acb4-cca4f4d56284]
[2019-11-11 19:53:46.285521] Received request ::[c2276a4e-5fe9-4a20-a4c8-cc12256a1535]
[2019-11-11 19:53:46.285521] Received request ::[02cdc0a7-db44-4769-b26b-9fab84fa27c1]
[2019-11-11 19:53:46.286519] Received request ::[b57c8eba-66dc-4916-bcfd-2ae8cd3bc2c2]
[2019-11-11 19:53:46.286519] Received request ::[d24d5dd5-f829-4c91-a49c-cd9cf69fa9e4]
[2019-11-11 19:53:46.286519] Received request ::[933827c0-89a6-4530-8dbb-ac35e8cfee5e]
[2019-11-11 19:53:46.286519] Received request ::[4ba88220-149a-4c7c-b8db-f975643c3c0d]
[2019-11-11 19:53:46.287518] Received request ::[86e67b0e-f39e-480c-b879-0d2715d37ae9]
[2019-11-11 19:53:46.287518] Received request ::[9b8f5a73-30d6-45f8-bedc-cda8bd1f90ec]
[2019-11-11 19:53:46.304434] Received request ::[8eab3b20-1e99-4849-b20c-39a48244c150]
[2019-11-11 19:53:46.305431] Received request ::[4adb32e4-926e-4d6c-9c85-56698b272a5c]
[2019-11-11 19:53:46.305431] Received request ::[70e01829-f76d-4b34-8b64-e44f8032e794]
[2019-11-11 19:53:46.314447] Received request ::[7d383913-6678-42ec-8c24-1aafdb080115]
[2019-11-11 19:53:46.314447] Received request ::[b04f0d0f-d9e0-48f7-82d2-170080bd1948]
[2019-11-11 19:53:46.315405] Received request ::[6fc73f70-8eef-4de3-a24d-1fc483a8d89e]
[2019-11-11 19:53:46.315405] Received request ::[23544862-de56-451f-b476-9031e72ad6d2]
[2019-11-11 19:53:46.316402] Received request ::[963eb793-8184-4cf5-be67-70e726272faa]
[2019-11-11 19:53:46.316402] Received request ::[09ed44aa-dd80-4044-a1b6-833d7b62ef5d]
[2019-11-11 19:53:46.316402] Received request ::[98ef481c-3dbc-44b8-b2f8-3d1267e9703a]
[2019-11-11 19:53:46.317400] Received request ::[ca61328f-0ab2-488f-b443-2dab5fc7fb90]
[2019-11-11 19:53:46.317400] Received request ::[4b58ced3-a2c1-4b5a-b6b5-0556c72abbaf]
[2019-11-11 19:53:46.317400] Received request ::[b64e7a96-d4c2-4e4f-a27c-5de1917090c5]
[2019-11-11 19:53:46.317400] Received request ::[854b53b3-d450-439b-a78e-d566a380d415]
[2019-11-11 19:53:46.317400] Received request ::[4ea32460-f516-4c4a-a056-f4bb1d82920d]
[2019-11-11 19:53:46.317400] Received request ::[6a2de88c-0e33-41c6-b7db-08dc51df246d]
[2019-11-11 19:53:46.317400] Received request ::[632f2b65-65ea-4e31-ba2a-3b65e702dd4f]
[2019-11-11 19:53:46.317400] Received request ::[e042b899-08e0-4118-83a1-b0a50a5399fc]
[2019-11-11 19:53:46.318397] Received request ::[4e1b2ba2-a73e-4113-bab2-d5e858a8782e]
[2019-11-11 19:53:46.344327] Received request ::[d4a2fc87-ae9c-4ccc-85cd-80e327d52860]
[2019-11-11 19:53:46.344327] Received request ::[a869da23-14ee-432e-95bb-5597ed489212]
[2019-11-11 19:53:46.344327] Received request ::[9f457aee-7c55-4080-9c9a-57493920b1c7]
[2019-11-11 19:53:46.344327] Received request ::[173ed748-8d35-49e0-bd53-613e8e47c24b]
[2019-11-11 19:53:46.344327] Received request ::[01d79b6d-90ea-4fb2-85b2-edbdb5e5ecd5]
[2019-11-11 19:53:46.344327] Received request ::[d929eec5-c09c-402a-8a85-b037f4c3363e]
[2019-11-11 19:53:46.345324] Received request ::[2566106e-e23d-40bd-8bc0-41312605472a]
[2019-11-11 19:53:46.349315] Received request ::[28ddaf23-2867-4019-8fd2-d1f746d90383]
[2019-11-11 19:53:46.349315] Received request ::[67a43476-3586-4699-83ba-755a9b16ff41]
[2019-11-11 19:53:46.349315] Received request ::[ebb780ed-fee1-4488-8fed-6d3bddf549f9]
[2019-11-11 19:53:46.350314] Received request ::[425b00d6-4c1f-4a77-9832-9c83976551ff]
[2019-11-11 19:53:46.350314] Received request ::[3e746313-a2e2-47ca-b7b1-c96c03ac1e57]
[2019-11-11 19:53:46.350314] Received request ::[c0b06c2b-42ec-40e7-96b4-3f1bd363c4ce]
[2019-11-11 19:53:46.350314] Received request ::[9a057ac0-4a07-4d20-b62b-b9f82d9ca4af]
[2019-11-11 19:53:46.350314] Received request ::[515c7e46-3fd0-457c-9427-fbcece3aabe5]
[2019-11-11 19:53:46.350314] Received request ::[f2e2f611-593d-45a8-b0a8-15856850e556]
[2019-11-11 19:53:46.351311] Received request ::[8cbca87e-0a85-49d2-9132-c2a91282088f]
[2019-11-11 19:53:46.351311] Received request ::[0c8eb454-02e1-433a-8c96-4cf3fe07908a]
[2019-11-11 19:53:46.351311] Received request ::[b653c500-a748-46b9-94f5-a07c741d4dd1]
[2019-11-11 19:53:46.351311] Received request ::[a9c3b49a-a543-4ad8-b3c0-31be27bb610d]
[2019-11-11 19:53:46.351311] Received request ::[9c0249f6-0b46-466c-8d72-d1e20570b1cc]
[2019-11-11 19:53:46.351311] Received request ::[b3b7c6ad-7aa1-403d-b9be-3ec75f47fe9c]
[2019-11-11 19:53:46.351311] Received request ::[c45d551c-48b4-4adc-b5ae-4d9bb81d5148]
[2019-11-11 19:53:46.351311] Received request ::[8e00a860-8c21-41d1-96d9-d4e7a72f4baa]
[2019-11-11 19:53:46.354301] Received request ::[dffbf81c-25a6-4539-a1b8-c80512008178]
[2019-11-11 19:53:46.354301] Received request ::[af8814f8-c72c-4215-a7a6-1b19e9e54167]
[2019-11-11 19:53:46.354301] Received request ::[01113a12-bada-430d-868a-b78ce6c81ef1]
[2019-11-11 19:53:46.355299] Received request ::[8c8537fe-f438-4d4e-9cf7-9e0eb77896b1]
[2019-11-11 19:53:46.355299] Received request ::[43e34a3a-1e60-4f3c-9f7e-c50816094cab]
[2019-11-11 19:53:46.355299] Received request ::[76ca1ca6-119e-44b8-b25b-aa9e1ecce829]
[2019-11-11 19:53:46.356295] Received request ::[8e76f63e-b1ad-47d5-a757-333521cef16c]
[2019-11-11 19:53:46.356295] Received request ::[576753b5-d70a-4b80-95f0-50ce1fe4dfaa]
[2019-11-11 19:53:46.357295] Received request ::[8ab48f3e-5ca6-4acb-ac84-cab82793d55e]
[2019-11-11 19:53:46.358293] Received request ::[fe13d115-01dc-4d6f-84a8-0154cecff4f2]
[2019-11-11 19:53:46.358293] Received request ::[b2973d32-fa3f-4b1f-b3f1-73126b55443d]
[2019-11-11 19:53:46.359290] Received request ::[997fc793-56c4-40a5-8315-2f4eb7e251d2]
[2019-11-11 19:53:46.359290] Received request ::[98b66d60-c6f7-4a25-8024-f027127f66f6]
[2019-11-11 19:53:46.360285] Received request ::[5e73e6e0-ad2e-4f74-ba25-9a6639223605]
[2019-11-11 19:53:46.360285] Received request ::[cb37e9d9-28c3-4e91-9eb6-d7fdd5a6e3af]
[2019-11-11 19:53:46.360285] Received request ::[d2f9366f-6987-4ca4-8d31-4bd7295066b6]
[2019-11-11 19:53:46.360285] Received request ::[d9320026-6dd1-4528-959f-930e24fe01b1]
[2019-11-11 19:53:46.360285] Received request ::[0da044b2-cb14-4d94-9983-f533888e404e]
[2019-11-11 19:53:46.360285] Received request ::[4ec4595b-a0db-4c77-8803-d2e3b762945a]
[2019-11-11 19:53:46.360285] Received request ::[c73be3e0-f235-438b-bf40-484196742ff3]
[2019-11-11 19:53:46.360285] Received request ::[eaaef86b-27ab-43fe-b199-461be2af7ad5]
[2019-11-11 19:53:46.360285] Received request ::[4e1cebbb-9658-444d-9fdd-ae4eac405776]
[2019-11-11 19:53:46.360285] Received request ::[e1f90d86-0a26-4cbd-9eb0-400557b46548]
[2019-11-11 19:53:46.360285] Received request ::[dfe99a8c-fcc1-4f10-ba74-bc3e1924a53a]
[2019-11-11 19:53:46.360285] Received request ::[1faff632-f2ed-471f-bba5-95b357e1b004]
[2019-11-11 19:53:46.360285] Received request ::[75bda90b-501b-4643-99b9-535e6fe346e5]
[2019-11-11 19:53:46.361318] Received request ::[887b2f3c-2a63-4f1a-924d-42dbb1a1da16]
[2019-11-11 19:53:46.361318] Received request ::[4bc9d83c-2376-42af-8bbb-b2c66f4fc17e]
[2019-11-11 19:53:46.361318] Received request ::[ec98b6cb-310d-4abf-823f-198bfd0e9f5f]
[2019-11-11 19:53:46.361318] Received request ::[0e42cccc-7c39-410f-ac47-4ecf1e007209]
[2019-11-11 19:53:46.361318] Received request ::[706b944b-5398-4dc4-8ce8-bec32b16d9e8]
[2019-11-11 19:53:46.361318] Received request ::[6ffad2fa-c794-424a-905e-af4bf2ab478c]
[2019-11-11 19:53:46.362278] Received request ::[7d9be490-5a70-42f0-8a28-95d36993ec35]
[2019-11-11 19:53:46.362278] Received request ::[b320112e-d3c3-448c-8dd0-3c2bdc6d5267]
[2019-11-11 19:53:46.362278] Received request ::[3b574d63-5f46-4448-bc8a-0531aa8bcd5a]
[2019-11-11 19:53:46.362278] Received request ::[3f565dde-4ccc-4fcf-aea9-d42a363785d1]
[2019-11-11 19:53:46.362278] Received request ::[444fa5b8-65de-45e8-bca3-1475c09e9de9]
[2019-11-11 19:53:46.362278] Received request ::[a0f3ccfb-05c4-4040-b034-97a8bb1c4464]
[2019-11-11 19:53:46.362278] Received request ::[a9cce902-91f7-4e9d-92f9-049cc3b7d287]
[2019-11-11 19:53:46.362278] Received request ::[74ead968-32b5-4403-8d13-447bec5fb5cf]
[2019-11-11 19:53:46.362278] Received request ::[f3c3d6f3-bd89-4d97-9725-70b953b8045c]
[2019-11-11 19:53:46.362278] Received request ::[1a88a16d-744e-4a4c-b27b-1650d661842c]
[2019-11-11 19:53:51.253110] Sending Response ::[{"result": "success", "id": "6cda0c89-7c34-4848-be05-8d30170bf247"}]
[2019-11-11 19:53:51.257849] Sending Response ::[{"result": "success", "id": "fbfbb2f7-4610-4d11-92f2-f4a828d4afee"}]
[2019-11-11 19:53:51.258847] Sending Response ::[{"result": "success", "id": "f6c07cb0-1246-47ac-b8c4-991753f74455"}]
[2019-11-11 19:53:51.258847] Sending Response ::[{"result": "success", "id": "409a3598-90d3-45ac-8651-aa5c301741f5"}]
[2019-11-11 19:53:51.282356] Sending Response ::[{"result": "success", "id": "9467a0ad-4dae-4e3b-b5a1-e2ace255d1df"}]
[2019-11-11 19:53:51.282356] Sending Response ::[{"result": "success", "id": "86e67b0e-f39e-480c-b879-0d2715d37ae9"}]
[2019-11-11 19:53:51.282356] Sending Response ::[{"result": "success", "id": "4ba88220-149a-4c7c-b8db-f975643c3c0d"}]
[2019-11-11 19:53:51.282356] Sending Response ::[{"result": "success", "id": "b025a616-c9a0-4211-9097-788373ac9b9e"}]
[2019-11-11 19:53:51.283352] Sending Response ::[{"result": "success", "id": "933827c0-89a6-4530-8dbb-ac35e8cfee5e"}]
[2019-11-11 19:53:51.283352] Sending Response ::[{"result": "success", "id": "d24d5dd5-f829-4c91-a49c-cd9cf69fa9e4"}]
[2019-11-11 19:53:51.283352] Sending Response ::[{"result": "success", "id": "b57c8eba-66dc-4916-bcfd-2ae8cd3bc2c2"}]
[2019-11-11 19:53:51.284406] Sending Response ::[{"result": "success", "id": "02cdc0a7-db44-4769-b26b-9fab84fa27c1"}]
[2019-11-11 19:53:51.284406] Sending Response ::[{"result": "success", "id": "5520c1ba-bd6d-4671-acb4-cca4f4d56284"}]
[2019-11-11 19:53:51.284406] Sending Response ::[{"result": "success", "id": "c2276a4e-5fe9-4a20-a4c8-cc12256a1535"}]
[2019-11-11 19:53:51.284406] Sending Response ::[{"result": "success", "id": "9b8f5a73-30d6-45f8-bedc-cda8bd1f90ec"}]
[2019-11-11 19:53:51.315765] Sending Response ::[{"result": "success", "id": "4ea32460-f516-4c4a-a056-f4bb1d82920d"}]
[2019-11-11 19:53:51.316772] Sending Response ::[{"result": "success", "id": "854b53b3-d450-439b-a78e-d566a380d415"}]
[2019-11-11 19:53:51.316772] Sending Response ::[{"result": "success", "id": "b64e7a96-d4c2-4e4f-a27c-5de1917090c5"}]
[2019-11-11 19:53:51.316772] Sending Response ::[{"result": "success", "id": "4b58ced3-a2c1-4b5a-b6b5-0556c72abbaf"}]
[2019-11-11 19:53:51.316772] Sending Response ::[{"result": "success", "id": "ca61328f-0ab2-488f-b443-2dab5fc7fb90"}]
[2019-11-11 19:53:51.317769] Sending Response ::[{"result": "success", "id": "98ef481c-3dbc-44b8-b2f8-3d1267e9703a"}]
[2019-11-11 19:53:51.317769] Sending Response ::[{"result": "success", "id": "09ed44aa-dd80-4044-a1b6-833d7b62ef5d"}]
[2019-11-11 19:53:51.317769] Sending Response ::[{"result": "success", "id": "963eb793-8184-4cf5-be67-70e726272faa"}]
[2019-11-11 19:53:51.317769] Sending Response ::[{"result": "success", "id": "23544862-de56-451f-b476-9031e72ad6d2"}]
[2019-11-11 19:53:51.317769] Sending Response ::[{"result": "success", "id": "6fc73f70-8eef-4de3-a24d-1fc483a8d89e"}]
[2019-11-11 19:53:51.318764] Sending Response ::[{"result": "success", "id": "b04f0d0f-d9e0-48f7-82d2-170080bd1948"}]
[2019-11-11 19:53:51.318764] Sending Response ::[{"result": "success", "id": "7d383913-6678-42ec-8c24-1aafdb080115"}]
[2019-11-11 19:53:51.318764] Sending Response ::[{"result": "success", "id": "70e01829-f76d-4b34-8b64-e44f8032e794"}]
[2019-11-11 19:53:51.318764] Sending Response ::[{"result": "success", "id": "4adb32e4-926e-4d6c-9c85-56698b272a5c"}]
[2019-11-11 19:53:51.318764] Sending Response ::[{"result": "success", "id": "8eab3b20-1e99-4849-b20c-39a48244c150"}]
[2019-11-11 19:53:51.319762] Sending Response ::[{"result": "success", "id": "4e1b2ba2-a73e-4113-bab2-d5e858a8782e"}]
[2019-11-11 19:53:51.319762] Sending Response ::[{"result": "success", "id": "e042b899-08e0-4118-83a1-b0a50a5399fc"}]
[2019-11-11 19:53:51.319762] Sending Response ::[{"result": "success", "id": "6a2de88c-0e33-41c6-b7db-08dc51df246d"}]
[2019-11-11 19:53:51.319762] Sending Response ::[{"result": "success", "id": "632f2b65-65ea-4e31-ba2a-3b65e702dd4f"}]
[2019-11-11 19:53:51.332735] Sending Response ::[{"result": "success", "id": "f2e2f611-593d-45a8-b0a8-15856850e556"}]
[2019-11-11 19:53:51.332735] Sending Response ::[{"result": "success", "id": "515c7e46-3fd0-457c-9427-fbcece3aabe5"}]
[2019-11-11 19:53:51.332735] Sending Response ::[{"result": "success", "id": "9a057ac0-4a07-4d20-b62b-b9f82d9ca4af"}]
[2019-11-11 19:53:51.333732] Sending Response ::[{"result": "success", "id": "c0b06c2b-42ec-40e7-96b4-3f1bd363c4ce"}]
[2019-11-11 19:53:51.333732] Sending Response ::[{"result": "success", "id": "3e746313-a2e2-47ca-b7b1-c96c03ac1e57"}]
[2019-11-11 19:53:51.333732] Sending Response ::[{"result": "success", "id": "425b00d6-4c1f-4a77-9832-9c83976551ff"}]
[2019-11-11 19:53:51.333732] Sending Response ::[{"result": "success", "id": "ebb780ed-fee1-4488-8fed-6d3bddf549f9"}]
[2019-11-11 19:53:51.334729] Sending Response ::[{"result": "success", "id": "67a43476-3586-4699-83ba-755a9b16ff41"}]
[2019-11-11 19:53:51.334729] Sending Response ::[{"result": "success", "id": "28ddaf23-2867-4019-8fd2-d1f746d90383"}]
[2019-11-11 19:53:51.334729] Sending Response ::[{"result": "success", "id": "2566106e-e23d-40bd-8bc0-41312605472a"}]
[2019-11-11 19:53:51.334729] Sending Response ::[{"result": "success", "id": "d929eec5-c09c-402a-8a85-b037f4c3363e"}]
[2019-11-11 19:53:51.335727] Sending Response ::[{"result": "success", "id": "01d79b6d-90ea-4fb2-85b2-edbdb5e5ecd5"}]
[2019-11-11 19:53:51.335727] Sending Response ::[{"result": "success", "id": "173ed748-8d35-49e0-bd53-613e8e47c24b"}]
[2019-11-11 19:53:51.335727] Sending Response ::[{"result": "success", "id": "9f457aee-7c55-4080-9c9a-57493920b1c7"}]
[2019-11-11 19:53:51.335727] Sending Response ::[{"result": "success", "id": "a869da23-14ee-432e-95bb-5597ed489212"}]
[2019-11-11 19:53:51.336724] Sending Response ::[{"result": "success", "id": "d4a2fc87-ae9c-4ccc-85cd-80e327d52860"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "8c8537fe-f438-4d4e-9cf7-9e0eb77896b1"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "1a88a16d-744e-4a4c-b27b-1650d661842c"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "a0f3ccfb-05c4-4040-b034-97a8bb1c4464"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "01113a12-bada-430d-868a-b78ce6c81ef1"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "eaaef86b-27ab-43fe-b199-461be2af7ad5"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "f3c3d6f3-bd89-4d97-9725-70b953b8045c"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "af8814f8-c72c-4215-a7a6-1b19e9e54167"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "dffbf81c-25a6-4539-a1b8-c80512008178"}]
[2019-11-11 19:53:51.353672] Sending Response ::[{"result": "success", "id": "8e00a860-8c21-41d1-96d9-d4e7a72f4baa"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "74ead968-32b5-4403-8d13-447bec5fb5cf"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "c45d551c-48b4-4adc-b5ae-4d9bb81d5148"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "b3b7c6ad-7aa1-403d-b9be-3ec75f47fe9c"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "444fa5b8-65de-45e8-bca3-1475c09e9de9"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "9c0249f6-0b46-466c-8d72-d1e20570b1cc"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "a9c3b49a-a543-4ad8-b3c0-31be27bb610d"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "b653c500-a748-46b9-94f5-a07c741d4dd1"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "4e1cebbb-9658-444d-9fdd-ae4eac405776"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "0c8eb454-02e1-433a-8c96-4cf3fe07908a"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "a9cce902-91f7-4e9d-92f9-049cc3b7d287"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "8cbca87e-0a85-49d2-9132-c2a91282088f"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "e1f90d86-0a26-4cbd-9eb0-400557b46548"}]
[2019-11-11 19:53:51.354707] Sending Response ::[{"result": "success", "id": "3f565dde-4ccc-4fcf-aea9-d42a363785d1"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "7d9be490-5a70-42f0-8a28-95d36993ec35"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "5e73e6e0-ad2e-4f74-ba25-9a6639223605"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "8ab48f3e-5ca6-4acb-ac84-cab82793d55e"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "6ffad2fa-c794-424a-905e-af4bf2ab478c"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "1faff632-f2ed-471f-bba5-95b357e1b004"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "4bc9d83c-2376-42af-8bbb-b2c66f4fc17e"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "75bda90b-501b-4643-99b9-535e6fe346e5"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "cb37e9d9-28c3-4e91-9eb6-d7fdd5a6e3af"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "dfe99a8c-fcc1-4f10-ba74-bc3e1924a53a"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "b320112e-d3c3-448c-8dd0-3c2bdc6d5267"}]
[2019-11-11 19:53:51.355702] Sending Response ::[{"result": "success", "id": "d9320026-6dd1-4528-959f-930e24fe01b1"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "c73be3e0-f235-438b-bf40-484196742ff3"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "4ec4595b-a0db-4c77-8803-d2e3b762945a"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "b2973d32-fa3f-4b1f-b3f1-73126b55443d"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "706b944b-5398-4dc4-8ce8-bec32b16d9e8"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "0da044b2-cb14-4d94-9983-f533888e404e"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "d2f9366f-6987-4ca4-8d31-4bd7295066b6"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "887b2f3c-2a63-4f1a-924d-42dbb1a1da16"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "98b66d60-c6f7-4a25-8024-f027127f66f6"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "8e76f63e-b1ad-47d5-a757-333521cef16c"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "76ca1ca6-119e-44b8-b25b-aa9e1ecce829"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "997fc793-56c4-40a5-8315-2f4eb7e251d2"}]
[2019-11-11 19:53:51.356702] Sending Response ::[{"result": "success", "id": "3b574d63-5f46-4448-bc8a-0531aa8bcd5a"}]
[2019-11-11 19:53:51.357698] Sending Response ::[{"result": "success", "id": "0e42cccc-7c39-410f-ac47-4ecf1e007209"}]
[2019-11-11 19:53:51.357698] Sending Response ::[{"result": "success", "id": "fe13d115-01dc-4d6f-84a8-0154cecff4f2"}]
[2019-11-11 19:53:51.357698] Sending Response ::[{"result": "success", "id": "576753b5-d70a-4b80-95f0-50ce1fe4dfaa"}]
[2019-11-11 19:53:51.357698] Sending Response ::[{"result": "success", "id": "ec98b6cb-310d-4abf-823f-198bfd0e9f5f"}]
[2019-11-11 19:53:51.357698] Sending Response ::[{"result": "success", "id": "43e34a3a-1e60-4f3c-9f7e-c50816094cab"}]

```

***```Asynchronous Rest API With Quart library:```*** 
-----------------------------------
- As Flask and Falcon don't support async by default, there is a popular library Quart which comes to a rescue.
- With same 5 second non blocking delay performance seems to be quite good. 
- Below has the entire logging trace with correlation id which actually shows how request been served asynchronously. 

***Server***

```python

[2019-11-11 20:03:56.866269] Inside in getInformation()
[2019-11-11 20:03:56.866269] Received request ::[dfdd8b87-2970-4de9-8227-6e3bbc9efe69]
[2019-11-11 20:03:56.866269] Inside in __doProcessing()
[2019-11-11 20:03:56.880230] Inside in getInformation()
[2019-11-11 20:03:56.880230] Received request ::[3608c28b-9ae2-49a8-921b-b6e7876ec40e]
[2019-11-11 20:03:56.880230] Inside in __doProcessing()
[2019-11-11 20:03:56.881229] Inside in getInformation()
[2019-11-11 20:03:56.882225] Received request ::[c9ddd22d-31b9-4734-8cf2-2ce7b1fe1cc2]
[2019-11-11 20:03:56.882225] Inside in __doProcessing()
[2019-11-11 20:03:56.882225] Inside in getInformation()
[2019-11-11 20:03:56.882225] Received request ::[cd3ef862-0927-4acb-85a7-cc849a39970b]
[2019-11-11 20:03:56.882225] Inside in __doProcessing()
[2019-11-11 20:03:56.898185] Inside in getInformation()
[2019-11-11 20:03:56.898185] Received request ::[3b0f8d4e-97ac-407f-8539-debccd74b2fc]
[2019-11-11 20:03:56.898185] Inside in __doProcessing()
[2019-11-11 20:03:56.900179] Inside in getInformation()
[2019-11-11 20:03:56.900179] Received request ::[03db5ea9-789c-4117-be65-1e0ecfca43a8]
[2019-11-11 20:03:56.900179] Inside in __doProcessing()
[2019-11-11 20:03:56.901177] Inside in getInformation()
[2019-11-11 20:03:56.901177] Received request ::[0186f688-657d-467a-8d1b-d214b13137a6]
[2019-11-11 20:03:56.901177] Inside in __doProcessing()
[2019-11-11 20:03:56.901177] Inside in getInformation()
[2019-11-11 20:03:56.901177] Received request ::[fba1efd5-4ae9-4228-9f8b-e8d6a989e27a]
[2019-11-11 20:03:56.901177] Inside in __doProcessing()
[2019-11-11 20:03:56.901177] Inside in getInformation()
[2019-11-11 20:03:56.901177] Received request ::[c8bba903-6560-4b65-af76-6c978e590332]
[2019-11-11 20:03:56.901177] Inside in __doProcessing()
[2019-11-11 20:03:56.913142] Inside in getInformation()
[2019-11-11 20:03:56.913142] Received request ::[083ceb43-b8c4-4bc4-9c27-955a572e2767]
[2019-11-11 20:03:56.913142] Inside in __doProcessing()
[2019-11-11 20:03:56.914139] Inside in getInformation()
[2019-11-11 20:03:56.915137] Received request ::[190aacbb-2405-4521-9cfb-2781c9fad2ad]
[2019-11-11 20:03:56.915137] Inside in __doProcessing()
[2019-11-11 20:03:56.917131] Inside in getInformation()
[2019-11-11 20:03:56.917131] Received request ::[5ceb8036-630c-4863-a7de-61e4f6138de6]
[2019-11-11 20:03:56.917131] Inside in __doProcessing()
[2019-11-11 20:03:56.917131] Inside in getInformation()
[2019-11-11 20:03:56.917131] Received request ::[250d0947-c213-4944-a621-6e4a8c79d0fa]
[2019-11-11 20:03:56.917131] Inside in __doProcessing()
[2019-11-11 20:03:56.917131] Inside in getInformation()
[2019-11-11 20:03:56.917131] Received request ::[2495dd27-3659-48ce-94d5-ef912503ed36]
[2019-11-11 20:03:56.917131] Inside in __doProcessing()
[2019-11-11 20:03:56.918130] Inside in getInformation()
[2019-11-11 20:03:56.918130] Received request ::[5dc05da2-7e51-4606-bbad-fdc1e20754f5]
[2019-11-11 20:03:56.919126] Inside in __doProcessing()
[2019-11-11 20:03:56.919126] Inside in getInformation()
[2019-11-11 20:03:56.919126] Received request ::[b4022289-f920-420e-bcd2-01184146d0a4]
[2019-11-11 20:03:56.919126] Inside in __doProcessing()
[2019-11-11 20:03:56.928102] Inside in getInformation()
[2019-11-11 20:03:56.928102] Received request ::[10edc7d6-eb45-44aa-92d1-d1350c5cb38c]
[2019-11-11 20:03:56.928102] Inside in __doProcessing()
[2019-11-11 20:03:56.929099] Inside in getInformation()
[2019-11-11 20:03:56.929099] Received request ::[24bdb6cd-8308-4a2d-95cd-894829f6247f]
[2019-11-11 20:03:56.929099] Inside in __doProcessing()
[2019-11-11 20:03:56.930097] Inside in getInformation()
[2019-11-11 20:03:56.930097] Received request ::[13dd14af-86e9-4ac3-9b1d-a477f2444c08]
[2019-11-11 20:03:56.930097] Inside in __doProcessing()
[2019-11-11 20:03:56.930097] Inside in getInformation()
[2019-11-11 20:03:56.930097] Received request ::[09e3de12-3b7a-4338-8dff-13ca11074ff0]
[2019-11-11 20:03:56.930097] Inside in __doProcessing()
[2019-11-11 20:03:56.930097] Inside in getInformation()
[2019-11-11 20:03:56.930097] Received request ::[7d7f8232-b1d0-402a-bcf6-0dbf3485eec1]
[2019-11-11 20:03:56.931094] Inside in __doProcessing()
[2019-11-11 20:03:56.932092] Inside in getInformation()
[2019-11-11 20:03:56.932092] Received request ::[726c1ea9-2051-45e9-96bd-8c420b3c9b08]
[2019-11-11 20:03:56.932092] Inside in __doProcessing()
[2019-11-11 20:03:56.932092] Inside in getInformation()
[2019-11-11 20:03:56.932092] Received request ::[bf8ecacb-2341-49df-b8d1-aac72e10d7b6]
[2019-11-11 20:03:56.932092] Inside in __doProcessing()
[2019-11-11 20:03:56.933089] Inside in getInformation()
[2019-11-11 20:03:56.933089] Received request ::[9cd3abac-0524-4a9f-9622-62bb91502ba4]
[2019-11-11 20:03:56.933089] Inside in __doProcessing()
[2019-11-11 20:03:56.933089] Inside in getInformation()
[2019-11-11 20:03:56.933089] Received request ::[c89ca09c-3272-4967-b930-a842cc1a1049]
[2019-11-11 20:03:56.933089] Inside in __doProcessing()
[2019-11-11 20:03:56.933089] Inside in getInformation()
[2019-11-11 20:03:56.933089] Received request ::[4ce86043-4203-413e-be4f-628ed2458bd7]
[2019-11-11 20:03:56.933089] Inside in __doProcessing()
[2019-11-11 20:03:56.934086] Inside in getInformation()
[2019-11-11 20:03:56.934086] Received request ::[da95270c-8be4-43c9-8b71-b9322ec71c33]
[2019-11-11 20:03:56.934086] Inside in __doProcessing()
[2019-11-11 20:03:56.934086] Inside in getInformation()
[2019-11-11 20:03:56.934086] Received request ::[7399b1ff-1591-4bf3-a2b9-b87eba478fb2]
[2019-11-11 20:03:56.934086] Inside in __doProcessing()
[2019-11-11 20:03:56.934086] Inside in getInformation()
[2019-11-11 20:03:56.934086] Received request ::[8c52f6ab-a841-40e1-be62-0a10f8a08be8]
[2019-11-11 20:03:56.934086] Inside in __doProcessing()
[2019-11-11 20:03:56.934086] Inside in getInformation()
[2019-11-11 20:03:56.934086] Received request ::[fb9105a8-fcca-4248-934c-7542b9ca5b2e]
[2019-11-11 20:03:56.935084] Inside in __doProcessing()
[2019-11-11 20:03:56.935084] Inside in getInformation()
[2019-11-11 20:03:56.935084] Received request ::[fb960b91-5a87-4cba-b356-164a69107b2e]
[2019-11-11 20:03:56.935084] Inside in __doProcessing()
[2019-11-11 20:03:56.935084] Inside in getInformation()
[2019-11-11 20:03:56.935084] Received request ::[accf4331-2d61-4893-b1bd-267496da4a73]
[2019-11-11 20:03:56.935084] Inside in __doProcessing()
[2019-11-11 20:03:56.943061] Inside in getInformation()
[2019-11-11 20:03:56.943061] Received request ::[9b03c028-c3df-41db-8214-71f478c55062]
[2019-11-11 20:03:56.943061] Inside in __doProcessing()
[2019-11-11 20:03:56.943061] Inside in getInformation()
[2019-11-11 20:03:56.943061] Received request ::[733b4e1b-1358-4e3a-91c7-d26db2f3334c]
[2019-11-11 20:03:56.943061] Inside in __doProcessing()
[2019-11-11 20:03:56.943061] Inside in getInformation()
[2019-11-11 20:03:56.943061] Received request ::[34f31cd1-feda-4d03-9a7a-d3e5253adc7e]
[2019-11-11 20:03:56.943061] Inside in __doProcessing()
[2019-11-11 20:03:56.943061] Inside in getInformation()
[2019-11-11 20:03:56.943061] Received request ::[153fd8c5-720d-489a-bd87-446f4adc6309]
[2019-11-11 20:03:56.943061] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[df2a8976-233c-4208-8c2c-8304f24b41ae]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[93a84abd-471e-40f8-891b-4f134dc014a6]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[7fec880c-8f09-4aa5-9ff4-792f5cac4d46]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[d63beca3-332c-479c-9731-6c3f2502ed82]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[fc56d438-157d-4490-96ad-9cff6a889b04]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.944059] Inside in getInformation()
[2019-11-11 20:03:56.944059] Received request ::[74cda2b2-1167-4a98-a9b8-6465cb49e5b8]
[2019-11-11 20:03:56.944059] Inside in __doProcessing()
[2019-11-11 20:03:56.945056] Inside in getInformation()
[2019-11-11 20:03:56.945056] Received request ::[5fa06d53-d855-4dc6-bcec-89e46c404430]
[2019-11-11 20:03:56.945056] Inside in __doProcessing()
[2019-11-11 20:03:56.945056] Inside in getInformation()
[2019-11-11 20:03:56.945056] Received request ::[eadd524c-7758-49b4-9e34-5353801b1670]
[2019-11-11 20:03:56.945056] Inside in __doProcessing()
[2019-11-11 20:03:56.945056] Inside in getInformation()
[2019-11-11 20:03:56.945056] Received request ::[61d5f138-d89f-4b62-971e-8900a90cfa87]
[2019-11-11 20:03:56.945056] Inside in __doProcessing()
[2019-11-11 20:03:56.950042] Inside in getInformation()
[2019-11-11 20:03:56.950042] Received request ::[c0647f12-3396-4f52-996e-6ef4e068060a]
[2019-11-11 20:03:56.950042] Inside in __doProcessing()
[2019-11-11 20:03:56.950042] Inside in getInformation()
[2019-11-11 20:03:56.950042] Received request ::[a5092544-7590-43dc-b7af-bf5a92089014]
[2019-11-11 20:03:56.950042] Inside in __doProcessing()
[2019-11-11 20:03:56.950042] Inside in getInformation()
[2019-11-11 20:03:56.950042] Received request ::[05c810d5-c799-48f0-9174-2bb831d7ddc7]
[2019-11-11 20:03:56.950042] Inside in __doProcessing()
[2019-11-11 20:03:56.950042] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[08a047a2-a0b8-4cfb-af2b-5787a8a47b40]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[a4bf36ee-90e1-43fe-9ac9-70fdae86d331]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[1887ba23-1b7e-4fd6-af58-b76779604082]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[18774248-2c72-432c-8e2a-ed34940462b4]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[591fc962-283e-4aae-9dbe-c8a00c153de8]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.951040] Received request ::[e81a97f0-9734-4379-b5a3-07e0a4c951a4]
[2019-11-11 20:03:56.951040] Inside in __doProcessing()
[2019-11-11 20:03:56.951040] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[10d9ee66-2456-48b2-84f5-4f5f29073cd5]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.952038] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[ca84ea26-0d68-4232-a757-b9c2f0d42a66]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.952038] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[27e1ccc8-24c6-418c-8573-40a45fddf8ae]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.952038] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[e28c9e9b-49c0-4ef1-8c04-88eb5c90af83]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.952038] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[22a778b4-8059-475f-abdf-706b0c9d3bee]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.952038] Inside in getInformation()
[2019-11-11 20:03:56.952038] Received request ::[1cbbcf52-8045-4d4c-bbb2-6a5e1187c36b]
[2019-11-11 20:03:56.952038] Inside in __doProcessing()
[2019-11-11 20:03:56.957024] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[12fd486f-b5b7-46bf-a48f-825456541f95]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.958021] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[d08ac915-de67-45ec-ba55-0d16c05769f2]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.958021] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[0f2037d7-d492-4b88-91a5-c3c4feb03a35]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.958021] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[77a53b2a-45fc-4f15-8302-7f5140691ef7]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.958021] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[da06a050-a0a2-4860-a4b6-178b05c76cff]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.958021] Inside in getInformation()
[2019-11-11 20:03:56.958021] Received request ::[7d12ae6b-8a99-4834-aa7c-6d5bd06be192]
[2019-11-11 20:03:56.958021] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[8827fabc-093f-4dfc-a8b9-0331f08f7e76]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[3082fca1-7b80-42d0-acf6-e914ceab83a7]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[e71ff121-09c7-4002-ae50-f477a7e62f1e]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[e23487b0-22fa-4386-abc8-45a7f2e51ba4]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[3cf6f4de-9dff-424e-9a67-c4aa81331bb9]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[20d1aeaa-1f00-480b-a570-fefcdf3f8684]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.959019] Inside in getInformation()
[2019-11-11 20:03:56.959019] Received request ::[8cb2f522-dad4-4261-ac49-fa6b8013f356]
[2019-11-11 20:03:56.959019] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[1cc2629b-de09-40cf-ac9a-8e9ad492206b]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[7e8fe9fa-80bc-4a28-a523-4f5172f178a3]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[8d9320d5-b198-4976-9b0b-03a21052f00f]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[9e6a7ea2-f252-4f0a-8739-4359ff0b7797]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[7da0a529-5cea-4d70-ba7d-71f8d220e7ac]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.960016] Received request ::[09cf9881-59be-4353-a1e9-23375e88b5f1]
[2019-11-11 20:03:56.960016] Inside in __doProcessing()
[2019-11-11 20:03:56.960016] Inside in getInformation()
[2019-11-11 20:03:56.961013] Received request ::[94e553ac-c4c9-454e-8b65-ecbbcfc0c3c9]
[2019-11-11 20:03:56.961013] Inside in __doProcessing()
[2019-11-11 20:03:56.961013] Inside in getInformation()
[2019-11-11 20:03:56.961013] Received request ::[13d2cade-1305-45f5-8e45-17966ce6ce31]
[2019-11-11 20:03:56.962492] Inside in __doProcessing()
[2019-11-11 20:03:56.962492] Inside in getInformation()
[2019-11-11 20:03:56.963056] Received request ::[31bc7e32-22ee-4dea-9912-6f6d6e052b2d]
[2019-11-11 20:03:56.963056] Inside in __doProcessing()
[2019-11-11 20:03:56.964044] Inside in getInformation()
[2019-11-11 20:03:56.964044] Received request ::[f1b3b01d-4aea-42a7-a836-d119d5c14acd]
[2019-11-11 20:03:56.964044] Inside in __doProcessing()
[2019-11-11 20:03:56.964044] Inside in getInformation()
[2019-11-11 20:03:56.964044] Received request ::[3233d917-9128-4530-b13f-bd916ff3e4d7]
[2019-11-11 20:03:56.964044] Inside in __doProcessing()
[2019-11-11 20:03:56.964044] Inside in getInformation()
[2019-11-11 20:03:56.964044] Received request ::[1cc52df5-4624-4803-8e29-916dec46a335]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[eeb1aff7-7c27-4f1d-bb50-e68353f5a701]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[331cd9ac-7fab-42bc-9686-392c2ac229e9]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[1ae7f89f-b06b-4ace-a5c8-7f8dea407645]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[f4542155-314a-45cd-920c-a7b6ca153b80]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[3c9eddb4-a4cd-4ad8-acd1-d6294ff39694]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.965043] Inside in getInformation()
[2019-11-11 20:03:56.965043] Received request ::[ebccda80-d73f-4f24-813a-f7cf082b8732]
[2019-11-11 20:03:56.965043] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.966037] Received request ::[15287c77-bf21-493c-99b2-f3a0fe25d43a]
[2019-11-11 20:03:56.966037] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.966037] Received request ::[c49954b3-0e63-4f8f-8924-4f42db30c420]
[2019-11-11 20:03:56.966037] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.966037] Received request ::[02b2cf9b-7ecf-4d16-95bb-4a0a6af01d16]
[2019-11-11 20:03:56.966037] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.966037] Received request ::[1aa9d7e1-f00e-4151-ae8e-447ee5292cef]
[2019-11-11 20:03:56.966037] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.966037] Received request ::[3f42ff3d-ef46-4319-8a4a-c45dff46b74e]
[2019-11-11 20:03:56.966037] Inside in __doProcessing()
[2019-11-11 20:03:56.966037] Inside in getInformation()
[2019-11-11 20:03:56.967034] Received request ::[975802d3-9abe-41fb-b535-859c813f827d]
[2019-11-11 20:03:56.967034] Inside in __doProcessing()
[2019-11-11 20:03:56.967034] Inside in getInformation()
[2019-11-11 20:03:56.967034] Received request ::[097fb9b0-9c2e-4c39-ab93-9db554bb52f4]
[2019-11-11 20:03:56.967034] Inside in __doProcessing()
[2019-11-11 20:03:56.967034] Inside in getInformation()
[2019-11-11 20:03:56.967034] Received request ::[168c7365-c962-4fa0-8e61-b88af3334c23]
[2019-11-11 20:03:56.967034] Inside in __doProcessing()
[2019-11-11 20:03:56.967034] Inside in getInformation()
[2019-11-11 20:03:56.967034] Received request ::[42cf4f31-a5cc-4dce-9334-f0eb1e23d725]
[2019-11-11 20:03:56.967034] Inside in __doProcessing()
[2019-11-11 20:04:01.862056] Sending Response ::[{"result": "success", "id": "dfdd8b87-2970-4de9-8227-6e3bbc9efe69"}]
[2019-11-11 20:04:01.863051] Sending Response ::[{"result": "success", "id": "cd3ef862-0927-4acb-85a7-cc849a39970b"}]
[2019-11-11 20:04:01.863051] Sending Response ::[{"result": "success", "id": "c9ddd22d-31b9-4734-8cf2-2ce7b1fe1cc2"}]
[2019-11-11 20:04:01.864047] Sending Response ::[{"result": "success", "id": "3608c28b-9ae2-49a8-921b-b6e7876ec40e"}]
[2019-11-11 20:04:01,866] 127.0.0.1:62166 GET /info 1.1 200 67 5000724
[2019-11-11 20:04:01,869] 127.0.0.1:62167 GET /info 1.1 200 67 4986810
[2019-11-11 20:04:01,872] 127.0.0.1:62169 GET /info 1.1 200 67 4990804
[2019-11-11 20:04:01,875] 127.0.0.1:62168 GET /info 1.1 200 67 4993798
[2019-11-11 20:04:01.911344] Sending Response ::[{"result": "success", "id": "3b0f8d4e-97ac-407f-8539-debccd74b2fc"}]
[2019-11-11 20:04:01.911344] Sending Response ::[{"result": "success", "id": "083ceb43-b8c4-4bc4-9c27-955a572e2767"}]
[2019-11-11 20:04:01.912340] Sending Response ::[{"result": "success", "id": "c8bba903-6560-4b65-af76-6c978e590332"}]
[2019-11-11 20:04:01.912340] Sending Response ::[{"result": "success", "id": "fba1efd5-4ae9-4228-9f8b-e8d6a989e27a"}]
[2019-11-11 20:04:01.912340] Sending Response ::[{"result": "success", "id": "0186f688-657d-467a-8d1b-d214b13137a6"}]
[2019-11-11 20:04:01.913337] Sending Response ::[{"result": "success", "id": "03db5ea9-789c-4117-be65-1e0ecfca43a8"}]
[2019-11-11 20:04:01.913337] Sending Response ::[{"result": "success", "id": "5ceb8036-630c-4863-a7de-61e4f6138de6"}]
[2019-11-11 20:04:01.913337] Sending Response ::[{"result": "success", "id": "190aacbb-2405-4521-9cfb-2781c9fad2ad"}]
[2019-11-11 20:04:01.914334] Sending Response ::[{"result": "success", "id": "24bdb6cd-8308-4a2d-95cd-894829f6247f"}]
[2019-11-11 20:04:01.914334] Sending Response ::[{"result": "success", "id": "b4022289-f920-420e-bcd2-01184146d0a4"}]
[2019-11-11 20:04:01.915331] Sending Response ::[{"result": "success", "id": "10edc7d6-eb45-44aa-92d1-d1350c5cb38c"}]
[2019-11-11 20:04:01.915331] Sending Response ::[{"result": "success", "id": "5dc05da2-7e51-4606-bbad-fdc1e20754f5"}]
[2019-11-11 20:04:01.916375] Sending Response ::[{"result": "success", "id": "2495dd27-3659-48ce-94d5-ef912503ed36"}]
[2019-11-11 20:04:01.916375] Sending Response ::[{"result": "success", "id": "250d0947-c213-4944-a621-6e4a8c79d0fa"}]
[2019-11-11 20:04:01,918] 127.0.0.1:62172 GET /info 1.1 200 67 5021136
[2019-11-11 20:04:01,921] 127.0.0.1:62176 GET /info 1.1 200 67 5007175
[2019-11-11 20:04:01,924] 127.0.0.1:62174 GET /info 1.1 200 67 5024130
[2019-11-11 20:04:01,926] 127.0.0.1:62173 GET /info 1.1 200 67 5027128
[2019-11-11 20:04:01,929] 127.0.0.1:62171 GET /info 1.1 200 67 5029123
[2019-11-11 20:04:01,932] 127.0.0.1:62170 GET /info 1.1 200 67 5033103
[2019-11-11 20:04:01,934] 127.0.0.1:62175 GET /info 1.1 200 67 5020141
[2019-11-11 20:04:01,936] 127.0.0.1:62180 GET /info 1.1 200 67 5022135
[2019-11-11 20:04:01,937] 127.0.0.1:62184 GET /info 1.1 200 67 5010168
[2019-11-11 20:04:01,939] 127.0.0.1:62181 GET /info 1.1 200 67 5022133
[2019-11-11 20:04:01,940] 127.0.0.1:62183 GET /info 1.1 200 67 5013158
[2019-11-11 20:04:01,941] 127.0.0.1:62179 GET /info 1.1 200 67 5026128
[2019-11-11 20:04:01,942] 127.0.0.1:62178 GET /info 1.1 200 67 5028123
[2019-11-11 20:04:01,943] 127.0.0.1:62177 GET /info 1.1 200 67 5029120
[2019-11-11 20:04:01.946281] Sending Response ::[{"result": "success", "id": "74cda2b2-1167-4a98-a9b8-6465cb49e5b8"}]
[2019-11-11 20:04:01.946281] Sending Response ::[{"result": "success", "id": "d63beca3-332c-479c-9731-6c3f2502ed82"}]
[2019-11-11 20:04:01.946281] Sending Response ::[{"result": "success", "id": "fc56d438-157d-4490-96ad-9cff6a889b04"}]
[2019-11-11 20:04:01.946281] Sending Response ::[{"result": "success", "id": "7fec880c-8f09-4aa5-9ff4-792f5cac4d46"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "93a84abd-471e-40f8-891b-4f134dc014a6"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "df2a8976-233c-4208-8c2c-8304f24b41ae"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "153fd8c5-720d-489a-bd87-446f4adc6309"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "34f31cd1-feda-4d03-9a7a-d3e5253adc7e"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "733b4e1b-1358-4e3a-91c7-d26db2f3334c"}]
[2019-11-11 20:04:01.947279] Sending Response ::[{"result": "success", "id": "9b03c028-c3df-41db-8214-71f478c55062"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "accf4331-2d61-4893-b1bd-267496da4a73"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "fb960b91-5a87-4cba-b356-164a69107b2e"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "fb9105a8-fcca-4248-934c-7542b9ca5b2e"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "8c52f6ab-a841-40e1-be62-0a10f8a08be8"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "7399b1ff-1591-4bf3-a2b9-b87eba478fb2"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "da95270c-8be4-43c9-8b71-b9322ec71c33"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "4ce86043-4203-413e-be4f-628ed2458bd7"}]
[2019-11-11 20:04:01.948277] Sending Response ::[{"result": "success", "id": "c89ca09c-3272-4967-b930-a842cc1a1049"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "9cd3abac-0524-4a9f-9622-62bb91502ba4"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "bf8ecacb-2341-49df-b8d1-aac72e10d7b6"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "726c1ea9-2051-45e9-96bd-8c420b3c9b08"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "7d7f8232-b1d0-402a-bcf6-0dbf3485eec1"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "09e3de12-3b7a-4338-8dff-13ca11074ff0"}]
[2019-11-11 20:04:01.949274] Sending Response ::[{"result": "success", "id": "13dd14af-86e9-4ac3-9b1d-a477f2444c08"}]
[2019-11-11 20:04:01,951] 127.0.0.1:62208 GET /info 1.1 200 67 5014155
[2019-11-11 20:04:01,952] 127.0.0.1:62199 GET /info 1.1 200 67 5015152
[2019-11-11 20:04:01,952] 127.0.0.1:62207 GET /info 1.1 200 67 5016150
[2019-11-11 20:04:01,953] 127.0.0.1:62198 GET /info 1.1 200 67 5017148
[2019-11-11 20:04:01,954] 127.0.0.1:62210 GET /info 1.1 200 67 5018145
[2019-11-11 20:04:01,955] 127.0.0.1:62213 GET /info 1.1 200 67 5018145
[2019-11-11 20:04:01,955] 127.0.0.1:62205 GET /info 1.1 200 67 5019142
[2019-11-11 20:04:01,956] 127.0.0.1:62204 GET /info 1.1 200 67 5021136
[2019-11-11 20:04:01,957] 127.0.0.1:62211 GET /info 1.1 200 67 5022133
[2019-11-11 20:04:01,958] 127.0.0.1:62203 GET /info 1.1 200 67 5022133
[2019-11-11 20:04:01,958] 127.0.0.1:62190 GET /info 1.1 200 67 5026123
[2019-11-11 20:04:01,959] 127.0.0.1:62189 GET /info 1.1 200 67 5027121
[2019-11-11 20:04:01,960] 127.0.0.1:62197 GET /info 1.1 200 67 5029115
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "5fa06d53-d855-4dc6-bcec-89e46c404430"}]
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "9e6a7ea2-f252-4f0a-8739-4359ff0b7797"}]
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "09cf9881-59be-4353-a1e9-23375e88b5f1"}]
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "8d9320d5-b198-4976-9b0b-03a21052f00f"}]
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "7e8fe9fa-80bc-4a28-a523-4f5172f178a3"}]
[2019-11-11 20:04:01.969186] Sending Response ::[{"result": "success", "id": "1cc2629b-de09-40cf-ac9a-8e9ad492206b"}]
[2019-11-11 20:04:01.969186][2019-11-11 20:04:01,961] 127.0.0.1:62191 GET /info 1.1 200 67 5030112
 [2019-11-11 20:04:01,961] 127.0.0.1:62185 GET /info 1.1 200 67 5030112
Sending Response ::[{"result": "success", "id": "8cb2f522-dad4-4261-ac49-fa6b8013f356"}][2019-11-11 20:04:01,962] 127.0.0.1:62195 GET /info 1.1 200 67 5031151

[2019-11-11 20:04:01,963] 127.0.0.1:62194 GET /info 1.1 200 67 5033104
[2019-11-11 20:04:01.970183][2019-11-11 20:04:01,964] 127.0.0.1:62193 GET /info 1.1 200 67 5034101
 [2019-11-11 20:04:01,965] 127.0.0.1:62182 GET /info 1.1 200 67 5035099
Sending Response ::[{"result": "success", "id": "20d1aeaa-1f00-480b-a570-fefcdf3f8684"}][2019-11-11 20:04:01,965] 127.0.0.1:62196 GET /info 1.1 200 67 5036097
[2019-11-11 20:04:01,966] 127.0.0.1:62187 GET /info 1.1 200 67 5037094

[2019-11-11 20:04:01,967] 127.0.0.1:62186 GET /info 1.1 200 67 5039089
[2019-11-11 20:04:01.971182][2019-11-11 20:04:01,968] 127.0.0.1:62192 GET /info 1.1 200 67 5039089
 [2019-11-11 20:04:01,968] 127.0.0.1:62188 GET /info 1.1 200 67 5040086
Sending Response ::[{"result": "success", "id": "3cf6f4de-9dff-424e-9a67-c4aa81331bb9"}]
[2019-11-11 20:04:01.971182] Sending Response ::[{"result": "success", "id": "e23487b0-22fa-4386-abc8-45a7f2e51ba4"}]
[2019-11-11 20:04:01.971182] Sending Response ::[{"result": "success", "id": "e71ff121-09c7-4002-ae50-f477a7e62f1e"}]
[2019-11-11 20:04:01.971182] Sending Response ::[{"result": "success", "id": "7da0a529-5cea-4d70-ba7d-71f8d220e7ac"}]
[2019-11-11 20:04:01.971182] Sending Response ::[{"result": "success", "id": "3082fca1-7b80-42d0-acf6-e914ceab83a7"}]
[2019-11-11 20:04:01.971182] Sending Response ::[{"result": "success", "id": "8827fabc-093f-4dfc-a8b9-0331f08f7e76"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "7d12ae6b-8a99-4834-aa7c-6d5bd06be192"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "da06a050-a0a2-4860-a4b6-178b05c76cff"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "77a53b2a-45fc-4f15-8302-7f5140691ef7"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "0f2037d7-d492-4b88-91a5-c3c4feb03a35"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "d08ac915-de67-45ec-ba55-0d16c05769f2"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "12fd486f-b5b7-46bf-a48f-825456541f95"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "1cbbcf52-8045-4d4c-bbb2-6a5e1187c36b"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "22a778b4-8059-475f-abdf-706b0c9d3bee"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "e28c9e9b-49c0-4ef1-8c04-88eb5c90af83"}]
[2019-11-11 20:04:01.972215] Sending Response ::[{"result": "success", "id": "27e1ccc8-24c6-418c-8573-40a45fddf8ae"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "ca84ea26-0d68-4232-a757-b9c2f0d42a66"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "10d9ee66-2456-48b2-84f5-4f5f29073cd5"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "e81a97f0-9734-4379-b5a3-07e0a4c951a4"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "591fc962-283e-4aae-9dbe-c8a00c153de8"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "18774248-2c72-432c-8e2a-ed34940462b4"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "1887ba23-1b7e-4fd6-af58-b76779604082"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "a4bf36ee-90e1-43fe-9ac9-70fdae86d331"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "08a047a2-a0b8-4cfb-af2b-5787a8a47b40"}]
[2019-11-11 20:04:01.973213] Sending Response ::[{"result": "success", "id": "05c810d5-c799-48f0-9174-2bb831d7ddc7"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "a5092544-7590-43dc-b7af-bf5a92089014"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "c0647f12-3396-4f52-996e-6ef4e068060a"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "61d5f138-d89f-4b62-971e-8900a90cfa87"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "eadd524c-7758-49b4-9e34-5353801b1670"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "c49954b3-0e63-4f8f-8924-4f42db30c420"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "3f42ff3d-ef46-4319-8a4a-c45dff46b74e"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "1aa9d7e1-f00e-4151-ae8e-447ee5292cef"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "ebccda80-d73f-4f24-813a-f7cf082b8732"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "f4542155-314a-45cd-920c-a7b6ca153b80"}]
[2019-11-11 20:04:01.974208] Sending Response ::[{"result": "success", "id": "331cd9ac-7fab-42bc-9686-392c2ac229e9"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "f1b3b01d-4aea-42a7-a836-d119d5c14acd"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "13d2cade-1305-45f5-8e45-17966ce6ce31"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "42cf4f31-a5cc-4dce-9334-f0eb1e23d725"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "3c9eddb4-a4cd-4ad8-acd1-d6294ff39694"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "097fb9b0-9c2e-4c39-ab93-9db554bb52f4"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "15287c77-bf21-493c-99b2-f3a0fe25d43a"}]
[2019-11-11 20:04:01.975206] Sending Response ::[{"result": "success", "id": "eeb1aff7-7c27-4f1d-bb50-e68353f5a701"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "168c7365-c962-4fa0-8e61-b88af3334c23"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "02b2cf9b-7ecf-4d16-95bb-4a0a6af01d16"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "1ae7f89f-b06b-4ace-a5c8-7f8dea407645"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "3233d917-9128-4530-b13f-bd916ff3e4d7"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "94e553ac-c4c9-454e-8b65-ecbbcfc0c3c9"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "1cc52df5-4624-4803-8e29-916dec46a335"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "975802d3-9abe-41fb-b535-859c813f827d"}]
[2019-11-11 20:04:01.976166] Sending Response ::[{"result": "success", "id": "31bc7e32-22ee-4dea-9912-6f6d6e052b2d"}]
[2019-11-11 20:04:01,977] 127.0.0.1:62209 GET /info 1.1 200 67 5040085
[2019-11-11 20:04:01,978] 127.0.0.1:62236 GET /info 1.1 200 67 5029115
[2019-11-11 20:04:01,979] 127.0.0.1:62238 GET /info 1.1 200 67 5030113
[2019-11-11 20:04:01,980] 127.0.0.1:62235 GET /info 1.1 200 67 5030113
[2019-11-11 20:04:01,980] 127.0.0.1:62234 GET /info 1.1 200 67 5032108
[2019-11-11 20:04:01,981] 127.0.0.1:62233 GET /info 1.1 200 67 5033107
[2019-11-11 20:04:01,982] 127.0.0.1:62247 GET /info 1.1 200 67 5034144
[2019-11-11 20:04:01,983] 127.0.0.1:62232 GET /info 1.1 200 67 5034144
[2019-11-11 20:04:01,983] 127.0.0.1:62246 GET /info 1.1 200 67 5035102
[2019-11-11 20:04:01,984] 127.0.0.1:62231 GET /info 1.1 200 67 5036098
[2019-11-11 20:04:01,985] 127.0.0.1:62245 GET /info 1.1 200 67 5037094
[2019-11-11 20:04:01,985] 127.0.0.1:62237 GET /info 1.1 200 67 5036097
[2019-11-11 20:04:01,986] 127.0.0.1:62230 GET /info 1.1 200 67 5039130
[2019-11-11 20:04:01,987] 127.0.0.1:62226 GET /info 1.1 200 67 5040086
[2019-11-11 20:04:01,987] 127.0.0.1:62229 GET /info 1.1 200 67 5040086
[2019-11-11 20:04:01,988] 127.0.0.1:62244 GET /info 1.1 200 67 5041120
[2019-11-11 20:04:01,989] 127.0.0.1:62228 GET /info 1.1 200 67 5042120
[2019-11-11 20:04:01,990] 127.0.0.1:62243 GET /info 1.1 200 67 5043118
[2019-11-11 20:04:01,990] 127.0.0.1:62227 GET /info 1.1 200 67 5044076
[2019-11-11 20:04:01,992] 127.0.0.1:62242 GET /info 1.1 200 67 5045073
[2019-11-11 20:04:01,992] 127.0.0.1:62218 GET /info 1.1 200 67 5050060
[2019-11-11 20:04:01,993] 127.0.0.1:62225 GET /info 1.1 200 67 5051095
[2019-11-11 20:04:01,994] 127.0.0.1:62217 GET /info 1.1 200 67 5052091
[2019-11-11 20:04:01,995] 127.0.0.1:62224 GET /info 1.1 200 67 5053054
[2019-11-11 20:04:01,995] 127.0.0.1:62216 GET /info 1.1 200 67 5053054
[2019-11-11 20:04:01,996] 127.0.0.1:62200 GET /info 1.1 200 67 5055046
[2019-11-11 20:04:01,997] 127.0.0.1:62223 GET /info 1.1 200 67 5056043
[2019-11-11 20:04:01,998] 127.0.0.1:62215 GET /info 1.1 200 67 5057043
[2019-11-11 20:04:01,998] 127.0.0.1:62222 GET /info 1.1 200 67 5057043
[2019-11-11 20:04:01,999] 127.0.0.1:62206 GET /info 1.1 200 67 5059034
[2019-11-11 20:04:02,000] 127.0.0.1:62214 GET /info 1.1 200 67 5060034
[2019-11-11 20:04:02,000] 127.0.0.1:62221 GET /info 1.1 200 67 5060034
[2019-11-11 20:04:02,002] 127.0.0.1:62220 GET /info 1.1 200 67 5061066
[2019-11-11 20:04:02,003] 127.0.0.1:62212 GET /info 1.1 200 67 5063025
[2019-11-11 20:04:02,004] 127.0.0.1:62219 GET /info 1.1 200 67 5065020
[2019-11-11 20:04:02,005] 127.0.0.1:62202 GET /info 1.1 200 67 5068011
[2019-11-11 20:04:02,006] 127.0.0.1:62201 GET /info 1.1 200 67 5069009
[2019-11-11 20:04:02,007] 127.0.0.1:62250 GET /info 1.1 200 67 5051058
[2019-11-11 20:04:02,008] 127.0.0.1:62252 GET /info 1.1 200 67 5050060
[2019-11-11 20:04:02,008] 127.0.0.1:62251 GET /info 1.1 200 67 5051057
[2019-11-11 20:04:02,009] 127.0.0.1:62249 GET /info 1.1 200 67 5053052
[2019-11-11 20:04:02,010] 127.0.0.1:62263 GET /info 1.1 200 67 5054049
[2019-11-11 20:04:02,010] 127.0.0.1:62261 GET /info 1.1 200 67 5055047
[2019-11-11 20:04:02,012] 127.0.0.1:62257 GET /info 1.1 200 67 5056046
[2019-11-11 20:04:02,013] 127.0.0.1:62240 GET /info 1.1 200 67 5063025
[2019-11-11 20:04:02,013] 127.0.0.1:62256 GET /info 1.1 200 67 5056044
[2019-11-11 20:04:02,014] 127.0.0.1:62248 GET /info 1.1 200 67 5058075
[2019-11-11 20:04:02,015] 127.0.0.1:62254 GET /info 1.1 200 67 5058038
[2019-11-11 20:04:02,016] 127.0.0.1:62264 GET /info 1.1 200 67 5059036
[2019-11-11 20:04:02,016] 127.0.0.1:62260 GET /info 1.1 200 67 5061030
[2019-11-11 20:04:02,017] 127.0.0.1:62255 GET /info 1.1 200 67 5060070
[2019-11-11 20:04:02,018] 127.0.0.1:62265 GET /info 1.1 200 67 5062029
[2019-11-11 20:04:02,019] 127.0.0.1:62262 GET /info 1.1 200 67 5063026
[2019-11-11 20:04:02,019] 127.0.0.1:62258 GET /info 1.1 200 67 5064059
[2019-11-11 20:04:02,021] 127.0.0.1:62239 GET /info 1.1 200 67 5071004
[2019-11-11 20:04:02,022] 127.0.0.1:62259 GET /info 1.1 200 67 5066017
[2019-11-11 20:04:02,023] 127.0.0.1:62253 GET /info 1.1 200 67 5065020
[2019-11-11 20:04:02,023] 127.0.0.1:62241 GET /info 1.1 200 67 5073995

```

Now, the question is what would happen of all the Synchronous implementation which has already been done. 
How to scale those without doing much modifications in code. Answer would be  

1) You can introduce a async layer in your service architecture. For an example : Celery 
   This gives a proper asynchronous task based system which would actually helps in performing
   async communication between services with correlation id. 
   One of the sample implementation can be seen in here : https://github.com/sughosneo/taskmgmt
   
2) Or, if task based implementation could be overkill trade off based on the user base and time constraint. 
Then you can introduce a think async language layer like node.js for your metadata handling and shift the core responsibility to your autonomous
python application services. So that most of the transactions would get taken care by the fast asyn rest API layer.
 
Then ofcourse above listed points could be useful extension of this coding exercise which can also be used to 
enhance the scalability.

References :
-------------------------------

[1] - [https://medium.com/@pgjones/quart-a-asyncio-alternative-to-flask-32666ae2abb0](https://medium.com/@pgjones/quart-a-asyncio-alternative-to-flask-32666ae2abb0)

[2] - [https://medium.com/cowrks/asynchronous-python-app-architecture-5395d5338c4a](https://medium.com/cowrks/asynchronous-python-app-architecture-5395d5338c4a)

[3] - [https://stackoverflow.com/questions/56729764/python-3-7-asyncio-sleep-and-time-sleep](https://stackoverflow.com/questions/56729764/python-3-7-asyncio-sleep-and-time-sleep)



   
   

 