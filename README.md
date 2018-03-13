# SoccerGAN
<table>
  <td>
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player1.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player2.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player3.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player4.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player5.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player6.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player7.png" width="64">
<img src="http://www.rosstaylor.xyz/content/images/2018/03/player8.png" width="64">
  <img src="http://www.rosstaylor.xyz/content/images/2018/03/player9.png" width="64"></td>
</table>
Generating soccer players using a WGAN-GP model. See the enclosed repository for the Jupyter Notebook used to construct these results. The accompanying blog post can be viewed at rosstaylor.xyz. 

## Training Details

Results were run using a p2.xlarge instance on AWS; training took around 15 hours. The dataset can be obtained [here](https://www.fmscout.com/a-df11-facepacks-2018.html). Trained for 100 epochs. I suspect you could get a lot better quality with more epochs. Additionally the full dataset has around 100,000 faces and I only used a third of these. So if you want to dedicate more compute and get better results, please knock yourself out!

<img src="http://www.rosstaylor.xyz/content/images/2018/03/output_2_201.png" width=300>

## Additional Credits

I looked at a number of existing implementations in TensorFlow with this project, particularly carpedm20's DCGAN implementation at https://github.com/carpedm20/DCGAN-tensorflow, and this may be reflected in some stylistic similarities in the code.

## Finally

If you liked what you saw and want to see more stuff like this:

**Twitter** : @rosstaylor90

**Send ETH love to** : 0x7d4AFAc854D58E5FDbbFeEb5fe678d6CB2d02207

**Donate to** : https://secure.greenpeace.org.uk/page/contribute/greenpeace-main
