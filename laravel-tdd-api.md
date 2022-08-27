# TDD를 사용한 Laravel API 구축

이 글의 목적은 TDD를 개인이나 팀의 워크플로우로 포함하는 것이 어렵거나 고통스러울 필요가 없으며 어디서부터 시작하고 무엇을 테스트해야 하는지 이해하도록 하는 것입니다.

TDD를 습관으로 받아들이고 나에게 맞는 워크플로우를 찾아야 하며 표준 워크플로를 갖는 것이 중요합니다. 일반적인 프로젝트에서 가장 먼저 수행할 작업을 알면 자신만의 구조를 만들고, 모든 것이 앱의 어디에 있는지 알 수 있는 방식으로 구성하고, 개인/클라이언트 프로젝트를 약간 표준화하는 데 도움이 될 수 있습니다.

즉, TDD는 더 빠르고 자신 있게 코딩하는 데 도움이 됩니다. 앞서 무엇을 먼저 테스트해야 하는지 이해해야 한다고 언급했지만 실제로는 중요하지 않습니다. 테스트는 다음 단계로 안내할 것이므로 진정으로 이해해야 할 것은 테스트하려는 기능뿐입니다.

### 다룰 내용

- 기본 CRUD 기능에 중점을 둔 API 생성
- 테스트 가능한 Laravel 애플리케이션 구축 방법을 설명하는 데 도움이 되도록 처음부터 TDD를 구현

### 요구사항

- 프레임워크에 대한 기본 지식
- 새로운 라라벨 프로젝트

이제 부동산 앱을 위한 API 를 만들 것입니다.

properties 테이블:

- id: primary key
- type: string
- price: unsigned integer
- description: text

4 API 함수:

- index
- store
- update
- delete

### Index 테스트

index 함수는 보통 Model의 특정 Collection을 반환하는 데 사용됩니다.

**우리가 할 테스트**

- API endpoint
- Collection 형태로 반환되는 response

자, 테스트를 생성해 봅니다. 터미널을 열고 라라벨 프로젝트에서 아래의 코드를 실행합니다.

```bash
php artisan make:test Api/PropertiesTest
```

그러면 /tests/Features/Api/PropertiesTest.php 와 같이 테스트 파일이 생성될 것입니다.

이 파일에 우리는 첫번째 테스트를 추가할 것입니다. 이 테스트는 우리가 index API 경로에 도달했는지 테스트하는 것이고 이 시점에서는 아직 갖고 있지 않은 Properties의 Collection을 가져오지만 테스트를 진행할 것입니다.

```php
<?php

namespace Tests\Feature\Api;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class PropertiesTest extends TestCase
{
	use RefreshDatabase;

	/** @test */
	public function can_get_all_properties()
	{
		// Create Property so that the response returns it.
		$property = Property::factory()->create();

		$response = $this->getJson(route('api.properties.index'));
		// We will only assert that the response returns a 200 status for now.
		$response->assertOk();
	}
}
```

물론 에러가 나타날 것입니다. 아직 **`Property`** 모델을 생성하지 않았으므로 프로젝트 디렉토리 내에서 **`./vendor/bin/phpunit --testdox`**
를 실행하면 다음과 같이 나타날 것입니다.

```bash
Tests\Feature\Api\PropertiesTest::can_get_all_properties
Error: Class 'Tests\Feature\Api\Property' not found
```

아래의 명령을 실행해 봅니다.

**`php artisan make:model Property -mf`**

위 명령은

- **`app/Models/Property.php`** 모델을 생성합니다.
- **`-m`** : **`/database/migrations`** 경로에 Migration 파일을 생성합니다.
- **`-f`** :  **`/database/factories`** 경로에 **`PropertyFactory.php`** 라는 Factory 클래스 파일을 생성합니다.

TDD 접근 방식에 따라 단계별로 진행할 것입니다. 모델, 마이그레이션 그리고 팩토리를 생성한 후 다시 테스트를 실행합니다.(테스트 위에 Property 모델 정의를 import하지 않으면 이와 같은 오류가 발생합니다):

```bash
Tests\Feature\Api\PropertiesTest::can_get_all_properties
Symfony\Component\Routing\Exception\RouteNotFoundException:
Route [api.properties.index] not defined.
```

### Store 테스트

### Update 테스트

### Delete 테스트

## 결론
