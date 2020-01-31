import { Controller, Get, Post, Body, Put, Param, Delete } from '@nestjs/common'
import { ApiTags, ApiOperation, ApiProperty } from '@nestjs/swagger'
import { PostModel } from './posts.model'

class CreatePostDto {
  @ApiProperty({
    description: '帖子标题',
  })
  readonly title: string

  @ApiProperty({
    description: '帖子内容',
  })
  readonly content: string
}

@Controller('posts')
@ApiTags('贴子')
export class PostsController {
  @Get()
  @ApiOperation({ summary: '文章列表' })
  async index() {
    return await PostModel.find()
    // return [{ id: 1 }, { id: 1 }, { id: 1 }, { id: 1 }]
  }

  @Post()
  @ApiOperation({ summary: '创建帖子' })
  create(@Body() createPostDto: CreatePostDto) {
    return {
      success: createPostDto,
    }
  }
  @Get(':id')
  @ApiOperation({ summary: '文章详情' })
  detail(@Param('id') id: string) {
    return {
      success: id,
    }
  }
  @Put(':id')
  @ApiOperation({ summary: '更新文章' })
  update(@Param('id') id: string, @Body() body: CreatePostDto) {
    return {
      success: body,
    }
  }
  @Delete(':id')
  @ApiOperation({ summary: '删除文章' })
  remove(@Param('id') id: string, @Body() body: CreatePostDto) {
    return {
      success: body,
    }
  }
}
