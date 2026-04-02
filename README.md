The precise placement of sound sources in the stereo field can be difficult to discern just through close listening. To address this, I have developed a computational approach to more precisely locate these aural images.

First, I employ the open-source source separation model, Demucs, which allows me to partition the final mix into four isolated tracks: vocals, bass, drums, and other. Following this, I utilize a Python script of my own creation which generates a line graph. This graph plots the average loudness between the two channels. Figure 1a shows a sample line graph of an isolated track, and Figure 1b shows a combined line graph of all the isolated tracks.

<div align="center">

![Figure 1a](https://github.com/user-attachments/assets/3e2e6200-6571-45c5-9c97-767e666f5a70)

**Figure 1a:** A line graph of the isolated vocals in "Eleanor Rigby"

![Figure 1b](https://github.com/user-attachments/assets/808708da-1751-469d-b107-46e3fdcf5461)

**Figure 1b:** A line graph of all four isolated tracks in "Eleanor Rigby"

</div>

When an isolated track consists of a single voice, this method of representation is highly effective in illustrating its location in the stereo field. However, the current state of separation models poses a challenge: they fall short in distinguishing multiple instances of the same instrument. For instance, if the final mix features two bassists, the "bass" track will contain both of these voices. To circumvent this limitation, I've designed another Python script, which generates a graphic visualization of panning in a given track. It achieves this by computing the spectrograms of both channels, and using the relative levels of the two channels at each frequency bin, pinpoints the location of that bin on the stereo image. The result is a heatmap that visualizes histograms over time where each histogram shows the distribution of panning values across frequencies for each time step. Figure 2a shows a sample heatmap of an isolated track, and Figure 2b shows a heatmap of the final mix. The results from these two scripts complement and enhance the close readings, highlighting details and ensuring a more comprehensive analysis.

<div align="center">

![Figure 2a](https://github.com/user-attachments/assets/fbecf663-4787-431d-a5b9-f5aa0dfddff2)

**Figure 2a:** A heatmap of the isolated vocals in "Eleanor Rigby"

![Figure 2b](https://github.com/user-attachments/assets/365e5810-61ea-4d5f-ae31-7eedd050969e)

**Figure 2b:** A heatmap of "Eleanor Rigby"

</div>

## Qualitative

While these graphs offer valuable insights, their interpretability can be challenging, and they may not always align seamlessly with the listening experience. A more intuitive representation of panning can be seen in William Moylan's recent publication, *Recording Analysis: How the Record Shapes the Song* (2020). In this book, Moylan introduces "stereo imaging graphs," which illustrate the location of instruments in the stereo field over time. Although informative, Moylan's representations are based solely on close listening and may lack the precision achieved through computational methods. By consulting the graphs I've generated as I create my own stereo imaging graphs, I can bridge this precision gap. Figure 3 shows a simple example of a stereo imaging graph.

<div align="center">

![Figure 3](https://github.com/user-attachments/assets/ca669ce8-996a-4aa7-9320-3a755a16e872)

**Figure 3:** An example of a stereo imaging graph

</div>

The horizontal axis of this graph represents time, and the vertical axis represents position. The further up on the vertical axis, the further to the left channel the sound source is. The letters L, C, and R denote the left, center, and right channels respectively, and instruments are marked in the key to the left. In this example, there are three instruments, each panned to a different location: the piano is panned left, the drums are panned center, and the guitar is panned right. An alternative way to read these graphs is to look at the graph counterclockwise. This can be seen in Figure 4. This orientation makes understanding panning more intuitive, but complicates reading the time axis.

<div align="center">

![Figure 4](https://github.com/user-attachments/assets/dba8ad5d-d804-4bc7-afbd-e3f24737e3e1)

**Figure 4:** An alternative way to read a stereo imaging graph

</div>

These stereo imaging graphs illustrate changes in panning over time, showing clear correlations between panning and form in music. In discussing form, Moore and Dockwray's article "The Establishment of the Virtual Performance Space in Rock" (2008) provides a useful reference. The article presents a taxonomy of mixes in rock songs from 1966 to 1972. This taxonomy delineates various classes of mixes, each identified by a unique arrangement of sound sources within the stereo field. For instance, in the diagonal mix, the drums, vocals, and bass are centered, and other sound sources are placed to either side. This taxonomy is excellent for categorizing whole songs, but the spatial configuration of a song varies at times.

By reimagining the taxonomy of mixes as a system for categorizing the varying spatial configurations in songs, it becomes simpler to chart the progression of panning throughout a track and comparatively assess the state of the stereo field at different intervals. I define a **stereoscape** to be a record of the locations of salient sound sources within a specific timeframe. Stereoscapes can range from homogeneous to heterogeneous where a homogeneous stereoscape is one in which the sound sources are relatively centered and a heterogeneous stereoscape is one in which sound sources are panned either left, right, or out to both sides. Maximal homogeneity occurs when all sound sources are completely centered while maximal heterogeneity occurs when all sound sources are completely panned to one side, meaning that no sound source is playing through the other channel.

Most stereoscapes lie somewhere in between, and their classification will ultimately rely on context. Consider a song that features centered vocals with bass and drums panned to opposite sides. Given the prominence of vocals in popular music, this stereoscape leans toward homogeneity. However, if the vocals were very quiet, then the stereoscape might lean towards heterogeneity. The classification process is highly subjective, as different listeners may perceive a certain timbre to be more or less prominent. Ultimately, classification will depend on where the listener hears the perceptual center of mass to be.

Locating a stereoscape between homogeneity and heterogeneity is useful for comparison's sake — highlighting whether a section of the song is mixed more homogeneously or heterogeneously than another. There are certain exceptions to this system. In some songs, sound sources may move continually, which Moore and Dockwray would classify as a dynamic mix (2010).

The relative heterogeneity or homogeneity of a stereoscape determines its **stability**, meaning that panning can be understood as an agent of tension and release in music. The more homogeneous a stereoscape, the more stable it tends to be, while the more heterogeneous a stereoscape, the more unstable it tends to be. Dynamic stereoscapes will tend to be even less stable than maximally heterogeneous stereoscapes. One might question what it means for a horizontal configuration of sound sources to be stable or unstable. Stability here is a function of our normative mode of hearing. When one is focused on listening to a certain sound, say during conversation, the tendency is to face toward the source of the sound. The default and most relaxed mode of listening is to listen to a centered sound source, equivalent to a homogeneous stereoscape. Though it is certainly possible to listen to a sound without facing its source, it is more difficult to concentrate on and is therefore less relaxed. Listening without facing a sound source is akin to seeing with one's peripheral vision. In the case of a maximally heterogeneous stereoscape, the difference between the ears is drastic, and represents a tense and unbalanced mode of listening. With headphones this effect is even more pronounced, as a truly unnatural experience is produced where an entire ear is cut off from sound.

A stable stereoscape can then resolve to an unstable stereoscape, which is a common opening gambit in popular music. Often, beginnings of songs will feature a heterogeneous stereoscape, where an instrumental introduction is panned left or right. The entrance of the vocals in the center resolves this arrangement into a homogeneous stereoscape. On a larger scale, verses and choruses share a similar relationship. Verses will tend to feature more heterogeneous stereoscapes while choruses will tend to be centered. In this way, space is a form-defining element of stereo-mixed popular music. Using stereo imaging graphs and my taxonomy of stereoscapes, I will explore the impact of panning on the listening experience as well as its interaction with form.
