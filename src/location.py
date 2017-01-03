# Copyright 2017 NeuStar, Inc.All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .check_json import CheckJSON

class Location:
	def __init__(self, ip_info):
		self.location = CheckJSON('Location', ip_info).key_valid()

	def info(self):
		"""Returns all location info as an object"""
		return self.location

	def dma(self):
		"""Returns DMA"""
		return CheckJSON('dma', self.location).key_valid()

	def region(self):
		"""Returns region"""
		return CheckJSON('dma', self.location).key_valid()