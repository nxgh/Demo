import { NestFactory } from '@nestjs/core'
import { AppModule } from './app.module'
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger'
import * as mongoose from 'mongoose'


async function bootstrap() {

  mongoose.connect('mongodb://blog_dev:password@localhost:27017/blog_dev', {
    useNewUrlParser: true,
    useFindAndModify: false,
    useCreateIndex: true
  })

  const app = await NestFactory.create(AppModule)

  

  const options = new DocumentBuilder()
    .setTitle('Cats example')
    .setDescription('The cats API description')
    .setVersion('1.0')
    .build()
  const document = SwaggerModule.createDocument(app, options)
  SwaggerModule.setup('api', app, document)

  await app.listen(3000)
}
bootstrap()
