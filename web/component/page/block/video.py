# encoding: utf-8

from mongoengine import StringField, ReferenceField, PointField, IntField

from marrow.package.loader import load

from .base import Block
from .video_ import render_video_block


class VideoBlock(Block):
	__icon__ = 'youtube-play'
	
	# Data Definition
	
	KINDS = [
			"place",
			"directions",
			"search",
			"view",
			"streetview",
		]
	
	STYLES = [
			"roadmap",
			"satellite",
		]
	
	video = StringField(db_field='v')
	
	# Data Portability
	
	def __json__(self):
		return dict(super(MapBlock, self).as_json,
				video = self.video,
			)
	
	def __html_stream__(self):
		return render_video_block(self)
	
	def __text__(self):
		return self.target.__text__()
