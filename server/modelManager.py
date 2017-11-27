
import numpy as np
import os
from keras.models import Model
from keras.layers import Input, merge, Convolution2D, MaxPooling2D, UpSampling2D
from keras.optimizers import Adam
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as K

class UnetModel():

	self.model = self.get_unet()
	self.model_checkpoint = ModelCheckpoint('unet.hdf5',monitor='loss',save_best_only=True)
	
	def loadModel(self):
		try:
			self.model.load_weights('./unet.hdf5')
		except Exception as e:
			print(e)

	def predict(self):
		try:
			
		except Exception as e:
			print(e)

	def trainModel(self,img_train,img_mask_train,img_mask_test):
		try:
			model.fit(imgs_train, imgs_mask_train, batch_size=2, nb_epoch=20, verbose=1, shuffle=True, callbacks=[self.model_checkpoint])
		except Exception as e:
			print(e)

	def evaluateModel(self):
		try:
		
		except Exception as e:
			print(e)
			
	def get_unet(self):
		try:
			inputs = Input((1,img_rows, img_cols))
			conv1 = Convolution2D(32, 3, 3, activation='relu', border_mode='same')(inputs)
			conv1 = Convolution2D(32, 3, 3, activation='relu', border_mode='same')(conv1)
			pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

			conv2 = Convolution2D(64, 3, 3, activation='relu', border_mode='same')(pool1)
			conv2 = Convolution2D(64, 3, 3, activation='relu', border_mode='same')(conv2)
			pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

			conv3 = Convolution2D(128, 3, 3, activation='relu', border_mode='same')(pool2)
			conv3 = Convolution2D(128, 3, 3, activation='relu', border_mode='same')(conv3)
			pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

			conv4 = Convolution2D(256, 3, 3, activation='relu', border_mode='same')(pool3)
			conv4 = Convolution2D(256, 3, 3, activation='relu', border_mode='same')(conv4)
			pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

			conv5 = Convolution2D(512, 3, 3, activation='relu', border_mode='same')(pool4)
			conv5 = Convolution2D(512, 3, 3, activation='relu', border_mode='same')(conv5)

			up6 = merge([UpSampling2D(size=(2, 2))(conv5), conv4], mode='concat', concat_axis=1)
			conv6 = Convolution2D(256, 3, 3, activation='relu', border_mode='same')(up6)
			conv6 = Convolution2D(256, 3, 3, activation='relu', border_mode='same')(conv6)

			up7 = merge([UpSampling2D(size=(2, 2))(conv6), conv3], mode='concat', concat_axis=1)
			conv7 = Convolution2D(128, 3, 3, activation='relu', border_mode='same')(up7)
			conv7 = Convolution2D(128, 3, 3, activation='relu', border_mode='same')(conv7)

			up8 = merge([UpSampling2D(size=(2, 2))(conv7), conv2], mode='concat', concat_axis=1)
			conv8 = Convolution2D(64, 3, 3, activation='relu', border_mode='same')(up8)
			conv8 = Convolution2D(64, 3, 3, activation='relu', border_mode='same')(conv8)

			up9 = merge([UpSampling2D(size=(2, 2))(conv8), conv1], mode='concat', concat_axis=1)
			conv9 = Convolution2D(32, 3, 3, activation='relu', border_mode='same')(up9)
			conv9 = Convolution2D(32, 3, 3, activation='relu', border_mode='same')(conv9)

			conv10 = Convolution2D(1, 1, 1, activation='sigmoid')(conv9)

			model = Model(input=inputs, output=conv10)

			model.compile(optimizer=Adam(lr=1.0e-5), loss=dice_coef_loss, metrics=[dice_coef])

			return model
		except Exception as e:
		print(e)
