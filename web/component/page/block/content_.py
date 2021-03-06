# encoding: cinje

: def render_text_block block, content
: classes = set(block.properties.get('cls', '').split())

: if 'width' in block.properties
	: classes.add('col-md-' + str(block.properties.width))
: end

<section&{id=block.properties.get('id', block.id), class_=classes, data_block=block.id, data_format=block.format, data_editable="yes"}>
	#{content}
</section>
