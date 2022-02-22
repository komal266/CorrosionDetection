# CorrosionDetection
Corrosion is defined as the deterioration of a material, usually a metal, because of reaction with its surrounding 
environment (Chilingarian, 1989; Popoola, Grema, Latinwo, Gutti, Balogun, 2013). The reaction can be known 
as the electrochemical process, which contains various solid and liquid substances. Corrosion can lead to the 
loss of the purity of the metal. When a metal structure undergoes corrosion, it loses its strength, and the 
tendency to experience structural collapse increases. For example, ships, tankers, pipelines, wind turbines, and 
concrete rebars are often subject to the dangerous effects of corrosion. A study by NACE [1] estimates the 
global annual cost of corrosion at US$2.5 trillion, which is about 3.4% of the worldwide GDP （2013). These 
numbers solely represent the direct costs such as forced shut-downs or accidents; neither individual safety nor 
environmental consequences are included. Therefore, effective corrosion control methods become highly 
critical in preventing the damaging effects of corrosion. Various methods are widely used in the industry to 
control and prevent corrosion. These methods include cathodic and anodic protection, corrosion inhibitors, 
material selection, application of internal and external protective coatings, corrosion monitoring, and 
inspections (Meresht, Farahani, & Neshati, 2011; Popoola et al., 2013; Samimi & Zarinabadi,2011). Early 
detection of structural degradation prior to failure does not only have financial benefits. Still, it can also prevent 
catastrophic collapses of structures and avoid harmful situations for both humans and the environment.
The recent improvements in Artificial Intelligence (A.I.) for object recognition are largely attributed to the 
emergence of deep learning artificial neural networks. As one of the major fields of A.I., deep learning mimics 
the working of the human brain in processing data for use in detecting objects, recognizing speech, and creating 
patterns for use in decision making. Deep learning has developed as the natural progression from 'shallow 
networks' to multi-layered networks of neurons that are able to transform representations (of data, including 
images) from simple to complex, with increasing layer depth [2]. For corrosion protection, the first step 
towards the maintenance of structures is the visual inspection. Nowadays, this is mainly done by humans to 
collect qualitative data. Despite that these inspectors are certificated and experienced, the performance of this 
time-consuming method is subjective and largely dependent on the experience and qualifications of the 
individual (Agdas et al., 2016).On top of that, some locations of structures are difficult or completely inaccessible because of safety reasons, 
such as deep-sea pipelines, oil tanks, wind turbines, and some hindering constructions. In this paper, 
supervised learning image classification towards the detection of corrosion is investigated. The purpose of this 
research is to support the inspectors during the visual corrosion inspection to quickly detect corrosion through 
images taken by the drone reaching the inaccessible locations without bringing the inspector's safety in danger. 
In addition, this research also aims to develop a human-level accuracy model for automated corrosion 
detection, thus increasing the visual inspection efficiency.
This study focuses on visually detecting corrosion. Corrosion is the deterioration of a metal and can be visually 
identified by its color and texture. Therefore, the first method uses traditional computer vision techniques to 
extract parts of images that include corrosion, based on their color. The second method employs deep learning. 
While humans pay attention to the shape of an object to identify it, deep learning computer vision algorithms 
focus on their texture instead. Based on this attribute of deep learning algorithms and the distinct texture of 
corrosion contrary to other metals, deep convolutional neural networks are used to detect corrosion on a 
laboratory environment. The third method is also approaching corrosion detection as a deep learning problem. 
It treats corrosion as an object in an image where there are many other objects and backgrounds. Using 
appropriate object detection algorithms, it tracks corrosion in real world images.
Color Tracking for Corrosion Detection


#Methdology
This method tracks corrosion based on its color. The process is created combining various traditional computer 
vision algorithms and is implemented using python and OpenCV.
Color detection applications sometimes require two HSV color ranges to be extracted. This happens when 
tracking an object that its Hue range is a combination of the upper and lower values of the HSV space (ex. Hue is 
in the range of [350, 10]). In these cases, the threshold operation of the input image takes place twice, once for 
each range, returning two masks. Then the masks are added, and the process continues as explained above. 
The steps of the process can be summarized in the following manner: 
1. Input an RGB image
2. Convert image to HSV color space 
3. Define the color range to be tracked 
4. Threshold the image to create a mask containing regions with the previously defined colors 
5. Dilate the mask’s detected regions to deal with missing pixels 
6. Visualize the corrosion areas detected in the mask 
7. Find the contours and draw them on the input image 
8. Calculate the total corroded area of the image 
9. Return the input image marking corroded regions

#Conclusion
This study focused on the topic of corrosion detection. The issue was approached taking into consideration the 
visual attributes of corrosion, which were identified as color and texture. Computer vision and deep learning 
algorithms were utilized to test three different solutions to the problem. Computer vision processes were used 
to create a color detection algorithm that detects corroded metallic surfaces based on their color. The algorithm 
was tested on real world images depicting a bulk carriers’ compartments. The images were taken during an 
inspection by seasoned surveyors. The results vary depending on which compartment the images depict. For 
example, in images of fuel oil tanks, the algorithm performs great, while on cargo holds that are usually painted 
maroon, a color similar to the one of corrosion, it fails to differentiate between the corroded region and the 
background. This means that the process is overly sensitive to the noise surrounding the region of interest. 
Therefore, the color tracking method can not be used as a universal solution to the problem. But due to its 
straightforward implementation and low computational power requirements, it can be applicable to certain 
compartments of a vesses yielding adequate results. Considering the drawbacks of a color-based solution, the 
study also tested textured based solutions. For this purpose, deep learning algorithms were employed, who are 
well known for their ability to detect the texture of images. To support training of supervised learning 
algorithms two datasets were created. The first solution employed a Convolution Neural Network that used 
transfer learning from ResNet50. The CNN was trained on laboratory images for a binary classification 
problem, trying to classify rusted and not rusted metals. The model achieved great performance of 94% on test 
data. Its results supported the hypothesis that the texture of corrosion was detected. To scale up the abilities of 
the model a sliding algorithm was created that cropped images in pieces and fed them to the model. This 
waycorrosion was classified and located in the image. However, this approach failed to scale to real world 
images of vessels due to the noisy backgrounds surrounding corroded regions. The laboratory dataset that was 
used for the binary classification, assumed that a not corroded region is a clean shiny metallic surface. The 
problem with this approach is that corrosion is usually surrounded by other structural and general failures, 
such as cracks, deformation and coat failing, that could confuse the model. Hence, a better algorithm is needed 
that does not assume the nature of a non-corroded region. It is preferred to assume during training that 
everything surrounding the corroded area is not corrosion. Towards this end, corrosion detection was 
approached as an object detection problem. A Single Shot Detector with Mobilenet v1 was used and it achieved 
a loss of 1.6, 76% detection success on the test data and a mean accuracy score of 85% on the detection boxes 
of test data. Overall, texture-based approaches are found to perform better than color-based ones. Deep 
learning algorithms achieve great performance on color detection with the object detection approach being 
superior to the binary classification approach. A key take away of this study is the importance of training data 
for deep learning models that are to be used in real world problems. Algorithms like the ones used are fine 
tuned in achieving great performance but this only solves one part of the problem. With corrosion being a state 
of the metallic surface, its attributes differ over different metals, conditions under which rust is created, the location of the rust in the vessel etc. Thus, a great generalization of image examples is required to consider all 
corrosion depictions that can be found onboard a vessel. Otherwise, a model that performs perfectly on certain 
vessel would fail to generalize on others Based on the above findings the following approaches are proposed for 
future studies on the visual detection of corrosion. First, the same methods could be used on different expanded 
datasets to test their validity on more complex examples. The models used for transfer learning and the 
transfer learning strategies that were employed could be altered. Also, an image segmentation approach is 
proposed. This operation ties every pixel in an image to an object. In the case of corrosion detection every pixel 
would be categorized to three classes, pixels belonging to the corroded region, pixels bordering the corroded 
region and surrounding pixels. As a result, the region will be located, and the shape would be extracted. This 
could be helpful in cases where small corroded regions are widely dispersed in the image and bounding boxes 
of traditional object detection algorithms fail to include them. Finally, it would be useful to extract the reduction 
of thickness that has occurred to the metal due to corrosion. With this information the corrosion could be 
classified as pitting or general corrosion, which are the main corrosion phenomena on ships, and based on CSR 
rules a risk analysis of the corroded region could be performed. This is possible following approaches like the 
unsupervised monocular depth estimation [35] from researchers of the University College of London, where 
using data from stereo cameras algorithms learn to predict the depth of the image.


#Reference
[1] NACEIMPAC:ECONOMICIMPACT.http://impact.nace.org/economic-impact.aspx
[2] A.Leibbrandtetall.“Climbing robot for corrosion monitoring of reinforced concrete structures”
DOI:10.1109/CARPI.2012.64733652nd International Conference on Applied Robotics for the Power
Industry (CARPI), 2012 
[3] JongSehLee, InhoHwang, Don-Hee ChoiSang-HyunHong, “Advanced Robot System for Automated
Bridge Inspection and Monitoring”, IABSE Symposium Report 12/2008;
DOI:10.2749/222137809796205557. 
[4] “Bridgeblownup,tobebuiltanew”,newsinenglish.no, 
http://www.newsinenglish.no/2015/02/23/bridge-blown-up-to-be-built-anew/
[5] GangJi, YehuaZhu, YongzhiZhang, “The Corroded Defect Rating System of Coating Material Based on
Computer Vision” Transactions on Edutainment VIII Springer Volume7220pp210-220
[6] FBonnín-Pascual, AOrtiz, “Detection of Cracks and Corrosion for Automated Vessels Visual Inspection”,
A.I. Research and Development:Proceedings of the 13th conference.
[7] N.Hwang, H.Son, C.Kim and C.Kim, “Rust Surface Area Determination Of Steel Bridge Component For
Robotic Grit-Blast Machine”, is arc 2013 Paper 305. 
[8] Moselhi,O. and Shehab-Eldeen,T. (2000)."Classification of Defects in Sewer Pipes Using Neural
Networks." J.Infrastruct. Syst., 10.1061/(ASCE)1076-0342(2000)6:3(97),97-104

