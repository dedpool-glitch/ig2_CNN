Objective
1. Pass image pairs (same emotion, different ethnicity) through your fine-tuned EmoNet.
2. Extract feature maps from convolutional layers.
3. Compare activations across ethnic groups to identify bias.
4. Suppress biased feature maps and analyze the effect.
5. Potentially re-train the model after suppression.

STEPS:

STEP 1: We need to do the following things initially, this is for preparing data for analysis.
1. Pairs of images with the same emotion but different ethnicity, consider black and white at the beginning.
2. Decide on how many ethnicities to compare, we'll mostly do it in pairs but yeah.

STEP 2: Pass image pairs through fine-tuned emonet and observe feature map activations.
1. Hook into specific convolutional layers, look at earlier layers in the network (e.g., conv2, conv3, conv4).
2. Store feature maps for comparison...
3. Ensure feature maps are normalized..

STEP 3: Compute difference metrics using feature maps, for each pair
1. Identify feature maps with consistent high variation across pairs.
2. Would have to visualize feature maps with heatmaps, would help validate our analysis.
3. Statistically would have to prove if differences are significant.

STEP 4: Suppress potentially biased features
For feature maps that show consistent bias:
1. Make their activations 0 or scale them down by some proportionate factor.
2. Check activation gap again post semi-suppression.
3. Compare accuracy/gap before/after suppression to observe any change.

STEP 5: Model training karna hai ya nahi decide. 
1. After suppression, evaluate if bias is reduced but accuracy remains stable.
2. If accuracy drops significantly, retrain the model with modified activations.
3. We have to create some sort of metric that tells us if suppression is effective or not.
4. Will we fine-tune it or re-train again from scratch.
